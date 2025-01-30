import streamlit as st
import pandas as pd
import requests
import io

# Set your backend FastAPI URL
API_URL = "http://your-fastapi-backend-url"  # Replace this with your actual backend URL

st.title("AI-Powered Document Q&A")
st.write("Upload an Excel file and ask questions about its content.")

# File Upload Section with increased file size limit (max 100MB)
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"], accept_multiple_files=False)

if uploaded_file:
    try:
        # Display the preview of the uploaded file
        df = pd.read_excel(uploaded_file)
        st.write("Preview of uploaded file:")
        st.dataframe(df.head())  # Show the first few rows
    except Exception as e:
        st.error(f"Error reading the file: {e}")

    # Send the file to the FastAPI backend
    if st.button("Process File"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(f"{API_URL}/upload/", files=files)

        if response.status_code == 200:
            st.success("File uploaded successfully!")
            filename = response.json()["filename"]
            st.session_state["filename"] = filename  # Store filename for later use
        else:
            st.error("Failed to upload the file. Please try again.")

# Q&A Section
st.write("### Ask a question about your document:")
user_query = st.text_input("Enter your question:")

if user_query and "filename" in st.session_state:
    payload = {"filename": st.session_state["filename"], "question": user_query}
    response = requests.post(f"{API_URL}/ask/", json=payload)

    if response.status_code == 200:
        answer = response.json().get("answer", "No answer found.")
        st.write("#### Answer:")
        st.info(answer)
    else:
        st.error("Error processing the request. Please try again.")
elif user_query:
    st.warning("Please upload a file first before asking a question.")
