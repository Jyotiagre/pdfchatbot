import streamlit as st
import requests

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Define the header text and style
header_text = "Chat with PDF files using Gemini🤖"
header_style = {
        'background-color': '#0000FF',
        'color': '#ffce00',
        'padding': '10px',
        'text-align': 'center',
        'font-size': '30px',
    }

# Create the header using st.markdown
st.markdown(f'<h1 style="{";".join([f"{key}:{value}" for key, value in header_style.items()])}">{header_text}</h1>',
                unsafe_allow_html=True)


# Using sidebar "with" notation
with st.sidebar:
    option = "data"
    uploaded_file = st.file_uploader("**Upload File**", type=["pdf","txt"])
    st.write("")
    is_upload = st.button('Upload Files')
    is_generate_embedding = st.button('Generate Embedding')

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask Questions ?")

if prompt:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    url = "http://127.0.0.1:8000/qna?question={}".format(prompt)
    response = requests.request("GET", url)
    response= response.json()
    with st.chat_message("assistant"):
        st.write(response.get('message'))
    st.session_state.messages.append({"role": "assistant", "content": response.get('message')})

if is_upload:
    # Upload the file to FastAPI if a file is uploaded
    if uploaded_file is not None:        
        # Send the file to FastAPI
        files = {'file': (uploaded_file.name, uploaded_file, uploaded_file.type)}
        response = requests.post("http://127.0.0.1:8000/upload/", files=files)
        
        if response.status_code == 200:
            st.success("File uploaded successfully!")
        else:
            st.error(f"Failed to upload file. Status code: {response.status_code}")

if is_generate_embedding:
    url = "http://127.0.0.1:8000/loadembeddings"
    with st.spinner("Processing..."):
        response = requests.request("GET", url)
        if response.status_code == 200:
            st.success("Embedding Created successfully!")
        else:
            st.error(f"Failed to Create Embedding. Status code: {response.status_code}")
