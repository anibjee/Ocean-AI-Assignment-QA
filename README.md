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
