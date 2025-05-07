import pytest

# Create your tests here.

def test_register_user(api_client):
    response = api_client.post("/api/auth/register/", {
        "username": "newuser",
        "password": "securepass123"
    })
    assert response.status_code == 201

def test_login_user(api_client, create_user):
    user = create_user(username="loginuser", password="mypassword")
    response = api_client.post("/api/auth/login/", {
        "username": "loginuser",
        "password": "mypassword"
    })
    assert "access" in response.data
    assert response.status_code == 200
