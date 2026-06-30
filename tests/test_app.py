from app import app

client = app.test_client()

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello from Flask!" in response.get_data(as_text=True)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "OK"

def test_test():
    response = client.get("/test")
    assert response.status_code == 200
    assert "It looks cool!" in response.get_data(as_text=True)
