# Autonomous QA Agent

An intelligent, autonomous QA agent capable of constructing a "testing brain" from project documentation and generating Selenium test scripts.

### Live Link:
    https://app-agent-frontend-qprzty7u2oryopoxrgaxve.streamlit.app/

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

## Testing Workflow

Follow these steps to test the application's core functionality:

### 1. Build the Knowledge Base
1.  Navigate to the **Knowledge Base** page in the sidebar.
2.  Upload the sample files from the `assets/` directory:
    - `product_specs.md` (Requirements)
    - `ui_ux_guide.txt` (Design standards)
    - `checkout.html` (Target application page)
3.  Click **"Build Knowledge Base"** and wait for the success message.

### 2. Generate Test Cases
1.  Go to the **Test Generation** page.
2.  Enter a feature description, for example:
    > "Generate positive and negative test cases for the discount code feature."
3.  Click **"Generate Test Cases"**.
4.  Review the generated test plan in the table.

### 3. Generate & Run Selenium Script
1.  Go to the **Script Generation** page.
2.  Select a test case from the dropdown menu (e.g., "TC-001: Valid Discount Code").
3.  Click **"Generate Selenium Script"**.
4.  Copy the generated Python code.
5.  Create a new file (e.g., `run_test.py`) and paste the code.
6.  **Important**: Update the `driver.get()` URL in the script to point to the absolute path of `assets/checkout.html` on your machine.
7.  Run the script:
    ```bash
    python run_test.py
    ```
8.  Watch the browser execute the test automatically!

## Project Structure
- `backend/`: FastAPI application and business logic.
- `frontend/`: Streamlit user interface.
- `assets/`: Sample project assets (checkout.html, specs).
- `data/`: Storage for uploaded files and vector database.

## Features
- **Knowledge Base Ingestion**: Upload docs and HTML to build a RAG-based knowledge base.
- **Test Case Generation**: Generate comprehensive test cases grounded in documentation.
- **Script Generation**: Convert test cases into executable Selenium Python scripts.
