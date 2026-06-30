from app import app

client = app.test_client()


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from Flask! 🚀 , I Achieved it, My First Milestone !!!" in response.data


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data == b"OK"


def test_test():
    response = client.get("/test")
    assert response.status_code == 200
    assert b"It looks cool!" in response.data
