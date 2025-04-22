import pytest

# Create your tests here.

def test_get_today_menu(api_client, user, token, restaurant, menu_today):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    response = api_client.get("/api/menus/today/")
    assert response.status_code == 200
    assert response.data != []

def test_vote_for_menu(api_client, user, token, menu_today):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    response = api_client.post("/api/votes/", {
        "menu_id": menu_today.id
    })
    assert response.status_code == 201

def test_double_vote_fails(api_client, user, token, menu_today):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    api_client.post("/api/votes/", {"menu_id": menu_today.id})
    response = api_client.post("/api/votes/", {"menu_id": menu_today.id})
    assert response.status_code == 400

def test_get_today_votes_summary(api_client, token, user, menu_today):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    api_client.post("/api/votes/", {"menu_id": menu_today.id})
    response = api_client.get("/api/votes/today/")
    assert response.status_code == 200
    assert "menu_id" in response.data[0]
