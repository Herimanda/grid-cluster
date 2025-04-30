from app import app

def test_home():
    with app.test_client() as client:
        response = client.get('/notes')
        assert response.status_code == 200
