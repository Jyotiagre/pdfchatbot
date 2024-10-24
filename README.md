# Gemini PDF Chatbot

Gemini PDF Chatbot is a Streamlit-based application that allows users to chat with a conversational AI model trained on PDF documents. The chatbot extracts information from uploaded PDF files and answers user questions based on the provided context.

## Features

- **PDF Upload:** Users can upload multiple PDF files.
- **Text Extraction:** Extracts text from uploaded PDF files.
- **Conversational AI:** Uses the Gemini conversational AI model to answer user questions.
- **Chat Interface:** Provides a chat interface to interact with the chatbot.

## Getting Started

Your application will be available at <http://localhost:8502>.

## Local Development

Follow these instructions to set up and run this project on your local machine.

   **Note:** This project requires Python 3.10 or higher.

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/jyotiagre/pdfchatbot.git
   ```

## Project Structure
- `data`: store uploaded pdf.
-`client.py`: Main application script.
-`README.md`: Project documentation.
-`requirements.txt`: Python packages required for working of the app.
-`server.py`: Backend uses FastAPI.


2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
   
## Dependencies
- streamlit
- google-generativeai
- python-dotenv
- langchain
- PyPDF2
- chromadb
- faiss-cpu
- langchain_google_genai
- langchain-community


3. **Run the Application:**

   ```bash
    `server.py`: python -m uvicorn api:app --reload
   ```
   
   ```bash
    `client.py`: python -m streamlit run client.py
   ```

4. **Upload PDFs:**
   - Use the sidebar to upload PDF files.
   - Click on "Submit & Process" to extract text and generate embeddings.

5. **Chat Interface:**
   - Chat with the AI in the main interface.


