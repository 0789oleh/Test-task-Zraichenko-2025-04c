import pytest

# Create your tests here.

import datetime

def test_create_restaurant(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    response = api_client.post("/api/restaurants/", {"name": "Pasta House"})
    assert response.status_code == 201

def test_upload_menu(api_client, admin_user, restaurant):
    api_client.force_authenticate(user=admin_user)
    today = datetime.date.today().isoformat()
    response = api_client.post(f"/api/restaurants/{restaurant.id}/menus/", {
        "date": today,
        "items": ["Pizza", "Salad"]
    }, format='json')
    assert response.status_code == 201
