# Video Demo Script: Autonomous QA Agent

**Target Duration:** ~10-12 Minutes (leaving buffer for the 15-minute limit)
**Goal:** Explain the code, approach, and workflow of the Autonomous QA Agent.

---

## 1. Introduction & Problem Statement (2 Minutes)
*   **Hook:** "Hi everyone. In modern software development, keeping test suites in sync with rapidly changing requirements is a massive challenge. Today, I'm presenting an **Autonomous QA Agent** that solves this by building a 'testing brain' directly from your project documentation."
*   **What it does:** Briefly explain that the agent ingests docs (specs, UI guides) and HTML, uses RAG (Retrieval-Augmented Generation) to understand features, and automatically writes robust Selenium Python scripts.
*   **Key Technologies:** Mention the stack:
    *   **Backend:** FastAPI
    *   **Frontend:** Streamlit
    *   **AI:** LangChain, ChromaDB (Vector Store), Groq (Llama 3.3 70B for high-speed inference).

## 2. Architecture & Approach (3 Minutes)
*   **Visual Aid:** (Optional) If you have a diagram, show it. If not, just explain the flow.
*   **The Pipeline:**
    1.  **Ingestion:** We upload files (`.md`, `.html`, `.txt`). The system chunks them and creates embeddings using `HuggingFaceEmbeddings`. These are stored in `ChromaDB`.
    2.  **Retrieval (RAG):** When you ask for a test case (e.g., "Test the discount feature"), the system retrieves the most relevant chunks from the vector store.
    3.  **Generation:**
        *   **Step 1 (Test Planning):** The LLM (Llama 3) uses the retrieved context to generate a structured JSON test plan.
        *   **Step 2 (Scripting):** The LLM takes a specific test case + the HTML source code and writes a Selenium script.
*   **Why this approach?**
    *   **Groundedness:** By using RAG, the tests are based on *actual* docs, not hallucinations.
    *   **Robustness:** We explicitly prompt the model to use robust selectors and best practices (like `WebDriverWait`).

## 3. Code Walkthrough (4 Minutes)
*   *Switch to your IDE (VS Code).*
*   **Project Structure:** Quickly show the folders (`backend`, `frontend`, `assets`).
*   **Backend Core (`backend/services`):**
    *   **`ingestion.py`**: Show how `RecursiveCharacterTextSplitter` and `Chroma` are used to build the knowledge base.
    *   **`rag.py`**: Highlight the `generate_test_cases` function. Show the prompt template—point out how we enforce JSON output for structured data.
    *   **`script_gen.py`**: This is the "magic" part. Show the prompt where we instruct the LLM to write Selenium code. Point out the specific instructions: "Use `WebDriverWait`", "Handle float comparisons", "Use substring matching for styles". This ensures the generated code isn't flaky.
*   **Frontend (`frontend/pages`):**
    *   Briefly show `2_Test_Generation.py` to show how we connect the UI to the backend API.

## 4. Live Demo (3 Minutes)
*   *Switch to the Browser (Streamlit App).*
*   **Step 1: Knowledge Base**
    *   Go to the "Knowledge Base" page.
    *   Upload `assets/product_specs.md`, `assets/ui_ux_guide.txt`, and `assets/checkout.html`.
    *   Click "Build Knowledge Base". Show the success messages.
*   **Step 2: Test Generation**
    *   Go to "Test Generation".
    *   Enter a prompt: *"Generate positive and negative test cases for the discount code feature."*
    *   Click "Generate".
    *   Show the resulting table of test cases. Point out how they reference the uploaded `product_specs.md`.
*   **Step 3: Script Generation**
    *   Go to "Script Generation".
    *   Select one of the test cases (e.g., the positive discount code case).
    *   Click "Generate Selenium Script".
    *   Wait for the code to appear.
*   **Step 4: Execution (The "Wow" Moment)**
    *   Copy the generated code.
    *   Paste it into a new file in VS Code (e.g., `demo_test.py`).
    *   **Crucial:** Update the `driver.get()` URL to point to your local `assets/checkout.html` file (copy path).
    *   Run the script: `python demo_test.py`.
    *   Watch the browser open, type the code, and close. Show the "✅ Test Passed!" output in the terminal.

## 5. Conclusion (1 Minute)
*   Summarize: "We went from raw documentation to a working, executable test script in minutes, without writing a single line of boilerplate code."
*   Future Improvements: Mention potential next steps like integrating with CI/CD or supporting more complex page interactions.
*   "Thank you for watching."

---

## Preparation Checklist
- [ ] Ensure `uvicorn backend.main:app --reload` is running.
- [ ] Ensure `streamlit run frontend/app.py` is running.
- [ ] Have the `assets/` folder open and ready to drag-and-drop.
- [ ] Test the flow once before recording to ensure no surprises!
