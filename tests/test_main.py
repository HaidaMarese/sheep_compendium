from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_sheep():
    response = client.get("/sheep/1")
    assert response.status_code == 200
    expected_data = {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }
    assert response.json() == expected_data

#  Test creating a new sheep
def test_create_sheep():
    new_sheep = {
        "id": 7,
        "name": "Sunny",
        "breed": "Suffolk",
        "sex": "ewe"
    }
    #TODO: Send a POST request to add the new sheep
    response = client.post("/sheep/", json=new_sheep)

    # TODO: Assert that the response  status code is 201 (Created)
    assert response.status_code == 201
    assert response.json() == new_sheep

    # TODO: Verify that the sheep was actually added by retrieving it by ID
    response = client.get("/sheep/7")
    assert response.status_code == 200
    assert response.json() == new_sheep

# Test updating an existing sheep's information
def test_update_sheep():
    updated_sheep = {
        "id": 1,
        "name": "Spicy",
        "breed": "Gotland",
        "sex": "ewe"
    }
    response = client.put("/sheep/1", json=updated_sheep)
    assert response.status_code == 200
    assert response.json() == updated_sheep

    # Verify the update took effect by retrieving the sheep
    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json() == updated_sheep

# Test deleting an existing sheep
def test_delete_sheep():
    response = client.delete("/sheep/2")
    assert response.status_code == 204

    # Verify deletion by attempting to retrieve the deleted sheep
    response = client.get("/sheep/2")
    assert response.status_code == 404

#  Test retrieving all sheep in the inventory
def test_read_all_sheep():
    response = client.get("/sheep/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
