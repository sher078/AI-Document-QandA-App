# AI-Powered-Document-QandA-App


## Overview

The "AI-Powered Document Q&A App" is an advanced question-answering (QA) application built using **FastAPI, OpenAI, and Streamlit**. This application allows users to upload Excel (.xlsx) documents and ask questions based on their content. It utilizes OpenAI's GPT models to provide accurate and context-aware answers.

## Features

- **Excel File Upload:** Users can upload Excel (.xlsx) files up to **30MB+** in size.
- **Query Processing:** Once a document is uploaded, users can ask questions related to its content.
- **Secure API Key Handling:** The app requires an OpenAI API key for processing, ensuring secure and authenticated access.
- **User-Friendly Interface:** Built with **Streamlit**, the app provides an interactive and responsive UI.
- **Fast Processing:** The backend is powered by **FastAPI**, ensuring quick responses and efficient handling of large files.

## Installation and Setup

### Running the Application Locally

Follow these steps to set up and run the app on your local machine:

### 1. Clone the Repository

Clone this repository to your local machine using:

```bash
git clone https://github.com/your-repository.git
cd your-repository
```

### 2. Install Dependencies

Ensure you have **Python 3.8+** installed. Then, install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Set Up OpenAI API Key

You must have an OpenAI API key to use this app. Set the key as an environment variable:

```bash
export OPENAI_API_KEY="your-openai-api-key"
```

Or, manually enter it in the code where required.

**API Key Link (for reference):**

```

### 4. Run the Backend (FastAPI)

Start the FastAPI backend server:

```bash
uvicorn backend:app --host 0.0.0.0 --port 8000
```

This will start the FastAPI server on `http://127.0.0.1:8000`.

### 5. Run the Frontend (Streamlit)

In another terminal, run the Streamlit application:

```bash
streamlit run frontend.py
```

This will launch the UI in your web browser.

## Deployment Instructions

To deploy the app, follow these steps:

### Deploying FastAPI Backend

1. Choose a cloud provider like **Render, AWS, or Railway**.
2. Deploy the FastAPI application and obtain the backend URL (e.g., `https://your-backend-url.com`).
3. Ensure that the backend can accept file uploads up to **30MB+**.

### Deploying Streamlit Frontend

1. Deploy the Streamlit app using **Streamlit Cloud** or **Heroku**.
2. Update the `API_URL` in the frontend code to match the deployed backend URL.
3. Test the file upload and Q&A features to ensure smooth interaction.

## How to Use

1. **Start the Application:** Open the app in your web browser after running Streamlit.
2. **Upload a Document:** Click on the file uploader to upload your Excel (.xlsx) file.
3. **Enter Your Query:** Once the document is uploaded, type your question in the input field.
4. **Provide OpenAI API Key:** Enter your OpenAI API key securely in the provided field.
5. **Get Answers:** Click 'Submit' to process your query. The app will display relevant answers based on the document content.

## Security Note

- The application uses a secure API key input method.
- Always keep your OpenAI API key confidential.
- Avoid hardcoding API keys in public repositories.

## Contributions

Contributions to this project are welcome! Fork the repository and submit a pull request with improvements or new features.

---

This document provides all the necessary details for setting up and using the AI-powered document Q&A application while ensuring security and efficiency.



