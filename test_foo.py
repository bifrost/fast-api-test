from fastapi.testclient import TestClient

# Import our app from main.py.
from foo import app

# Instantiate the testing client with our app.
client = TestClient(app)

# Write tests using the same syntax as with the requests module.
def test_get_path():
    r = client.get("/items/0")
    assert r.status_code == 200

def test_get_malformed():
    r = client.get("/items/")
    assert r.status_code != 200