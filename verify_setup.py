import os
import sys
from fastapi.testclient import TestClient
from backend.main import app

# Add project root to path
sys.path.append(os.getcwd())

client = TestClient(app)

def test_backend_logic():
    print("1. Testing Root Endpoint...")
    response = client.get("/")
    assert response.status_code == 200
    print("   ✅ Root endpoint is up.")

    # Note: We cannot fully test ingestion and generation without the API Key and actual files.
    # This script verifies that the endpoints are reachable and the code imports correctly.
    
    print("\n2. Testing Ingestion Endpoint (Mock)...")
    # We won't actually upload to avoid side effects or auth errors, 
    # but we can check if the endpoint exists.
    # A 422 Unprocessable Entity is expected if we send no data, which means the endpoint is there.
    response = client.post("/api/v1/ingest/upload")
    assert response.status_code == 422
    print("   ✅ Ingestion endpoint is reachable.")

    print("\n3. Testing Test Case Generation Endpoint (Mock)...")
    response = client.post("/api/v1/generate/test-cases", json={})
    assert response.status_code == 422 # Missing field
    print("   ✅ Test Case Generation endpoint is reachable.")

    print("\n4. Testing Script Generation Endpoint (Mock)...")
    response = client.post("/api/v1/generate/script", json={})
    assert response.status_code == 422 # Missing field
    print("   ✅ Script Generation endpoint is reachable.")

    print("\n✅ Basic verification complete. The application structure is correct.")
    print("   To fully verify, please run the application and use the Streamlit UI with a valid GROQ_API_KEY.")

if __name__ == "__main__":
    test_backend_logic()
