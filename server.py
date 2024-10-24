from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.gemini import Gemini
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import globalVariable as gv

# Set up environment variable
import os
os.environ["GOOGLE_API_KEY"]="AIzaSyAyFiUTy4Bj0GOQ0ufJ09wA5lIjz5UsTmM"

app = FastAPI()

# Specify the folder where files will be stored
UPLOAD_FOLDER = "data"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
embed_model_uae = HuggingFaceEmbedding(model_name="WhereIsAI/UAE-Large-V1")
# intailise the language model
llm = Gemini()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"{UPLOAD_FOLDER}/{file.filename}"
    
    # Save the file to the specified folder
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return JSONResponse(content={"filename": file.filename, "message": "File uploaded successfully."})


@app.get("/loadembeddings")
async def load_embeddings():
    # Load documents
    documents = SimpleDirectoryReader("data").load_data()
    Settings.llm = llm
    Settings.embed_model = embed_model_uae
    Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
    Settings.num_output = 512
    Settings.context_window = 3900

    # a vector store index only needs an embed model
    gv.vectorstore = VectorStoreIndex.from_documents(
        documents, embed_model=embed_model_uae, 
    )

    # Persisting data to temporary store index and not make one for every query
    gv.vectorstore.storage_context.persist()

    return JSONResponse(content={"message": "Embedding Created successfully."})

@app.get("/qna")
async def answer_question(question:str):
    # Queries your Data from made up index database of your document
    query_engine = gv.vectorstore.as_query_engine(llm=llm)
    # Perform a query on the indexed documents
    answer = query_engine.query(question)
    return JSONResponse(content={"message": answer.response})