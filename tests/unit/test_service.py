# tests/unit/test_services.py
from app.services.user_service import create_user
from app.schemas import UserCreate

def test_create_user(db):
    # Arrange
    user_data = UserCreate(email="test@example.com", password="password")
    
    # Act
    user = create_user(db, user_data)
    
    # Assert
    assert user.email == "test@example.com"
    assert hasattr(user, "id")