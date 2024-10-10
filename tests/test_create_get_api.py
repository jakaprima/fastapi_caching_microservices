import random
import string
from fastapi.testclient import TestClient
from app import main


client = TestClient(main.app)

def random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def test_create_payload():
    response = client.post("/payload", json={
        "list_1": [random_string() for _ in range(3)],
        "list_2": [random_string() for _ in range(3)]
    })
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_payload():
    response = client.get("/payload/1")
    assert response.status_code == 200
    assert "output" in response.json()
