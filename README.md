# Autonomous QA Agent

An intelligent, autonomous QA agent capable of constructing a "testing brain" from project documentation and generating Selenium test scripts.

## Setup Instructions

### Prerequisites
- Python 3.9+
- Chrome Browser (for Selenium)

### Installation

1.  **Clone the repository** (or navigate to the project directory).
2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    # source venv/bin/activate # Mac/Linux
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Environment Variables**:
    Create a `.env` file in the root directory and add your API keys:
    ```
    GROQ_API_KEY=your_groq_api_key_here
    ```

## Usage

### Running the Backend
Start the FastAPI server:
```bash
uvicorn backend.main:app --reload
```
The API will be available at `http://localhost:8000`.

### Running the Frontend
Start the Streamlit UI:
```bash
streamlit run frontend/app.py
```
The UI will open in your browser at `http://localhost:8501`.

## Project Structure
- `backend/`: FastAPI application and business logic.
- `frontend/`: Streamlit user interface.
- `assets/`: Sample project assets (checkout.html, specs).
- `data/`: Storage for uploaded files and vector database.

## Features
- **Knowledge Base Ingestion**: Upload docs and HTML to build a RAG-based knowledge base.
- **Test Case Generation**: Generate comprehensive test cases grounded in documentation.
- **Script Generation**: Convert test cases into executable Selenium Python scripts.

## Running Generated Scripts
After generating a script (e.g., `test_discount.py`) from the UI:
1.  Save the script to your local machine (e.g., in the `assets/` folder).
2.  Run it using Python:
    ```bash
    python assets/test_discount.py
    ```
    *Note: Ensure you have the `assets/checkout.html` file available locally as the script will try to open it.*

## Deployment

This guide explains how to deploy the **Backend on Render** and the **Frontend on Streamlit Community Cloud**. This is the simplest "no-Docker" approach.

### Prerequisites
1.  A [GitHub](https://github.com) account.
2.  A [Render](https://render.com) account.
3.  A [Streamlit Community Cloud](https://share.streamlit.io/) account.
4.  Your `GROQ_API_KEY`.

### Concept: One Repo, Two Services
You will connect the **same GitHub repository** to both Render (Backend) and Streamlit (Frontend).
*   **Render** will see all files but only run the backend command (`uvicorn ...`).
*   **Streamlit** will see all files but only run the frontend app (`streamlit run ...`).
*   This is a standard "Monorepo" setup and works perfectly.

### Step 1: Push Code to GitHub
1.  Initialize a git repository (if not already done):
    ```bash
    git init
    git add .
    git commit -m "Ready for deployment"
    ```
2.  Create a new repository on GitHub.
3.  Push your code:
    ```bash
    git remote add origin <your-repo-url>
    git push -u origin main
    ```

### Step 2: Deploy Backend on Render
1.  Log in to [Render](https://dashboard.render.com/).
2.  Click **New +** -> **Web Service**.
3.  Connect your GitHub repository.
4.  **Configure Settings**:
    *   **Name**: `qa-agent-backend`
    *   **Runtime**: `Python 3`
    *   **Build Command**: `pip install -r requirements.txt`
    *   **Start Command**: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
5.  **Environment Variables** (Advanced):
    *   Add `GROQ_API_KEY`: Paste your key.
    *   Add `PYTHON_VERSION`: `3.9.0` (optional, but good for stability).
6.  Click **Create Web Service**.
7.  **Copy the URL**: Once deployed, copy the URL (e.g., `https://qa-agent-backend.onrender.com`).

### Step 3: Deploy Frontend on Streamlit Cloud
1.  Log in to [Streamlit Community Cloud](https://share.streamlit.io/).
2.  Click **New app**.
3.  Select your GitHub repository.
4.  **Main file path**: `frontend/app.py`
5.  **Advanced settings** -> **Secrets**:
    *   Add the following line (replace with your Render Backend URL):
        ```toml
        API_URL = "https://qa-agent-backend.onrender.com/api/v1"
        ```
        *Note: Make sure to add `/api/v1` at the end.*
6.  Click **Deploy**.

### Step 4: Verify
1.  Open your Streamlit App URL.
2.  Go to **Knowledge Base** and try uploading files.
3.  If it works, your Frontend is successfully talking to your Backend on Render!

### Troubleshooting
*   **Backend 502/503**: Check Render logs. It might be installing dependencies.
*   **Frontend Connection Error**: Ensure the `API_URL` secret in Streamlit Cloud is correct and includes `/api/v1`.
