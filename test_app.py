# test_app.py
from app import app

def test_hello():
    """Test that the hello route returns welcome message."""
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data

def test_health():
    """Test that the health route returns OK."""
    response = app.test_client().get('/health')
    assert response.status_code == 200
    assert b"OK" in response.data

def test_root_content():
    """Test that the root route returns a string."""
    response = app.test_client().get('/')
    assert isinstance(response.data, bytes)
    assert len(response.data) > 0