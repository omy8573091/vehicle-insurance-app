# tests/integration/test_api.py
def test_create_user(client):
    # Arrange
    user_data = {"email": "test@example.com", "password": "password"}
    
    # Act
    response = client.post("/users/", json=user_data)
    
    # Assert
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["email"] == "test@example.com"