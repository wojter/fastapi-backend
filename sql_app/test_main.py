from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_get_titles():
    response = client.get('/titles')
    assert response.status_code == 200


def test_read_title():
    title_id = 4
    response = client.get(f'/titles/{title_id}')
    assert response.status_code == 200
    res_data = response.json()
    assert res_data["id"] == title_id


def test_read_inexistent_titleId():
    response = client.get("/titles/0")
    assert response.status_code == 400
    assert response.json() == {'detail': 'Wrong title id'}


def test_read_inexistent_titleId_string():
    response = client.get("/titles/string")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "path",
                    "title_id"
                ],
                "msg": "value is not a valid integer",
                "type": "type_error.integer"
            }
        ]
    }


def test_create_title():
    new_title_data = {
        "title": "Test title",
        "type": "TYPE",
        "description": "Expamlpe desc",
        "runtime": 68,
        "release_year": 2012,
    }

    response = client.post('/titles',
                           json=new_title_data)
    assert response.status_code == 201
    res_data = response.json()

    assert "id" in res_data
    new_title_id = res_data["id"]
    for i in new_title_data:
        assert res_data[i] == new_title_data[i]

    response = client.get(f"/titles/{new_title_id}")
    assert response.status_code == 200
    res_data = response.json()
    assert res_data["id"] == new_title_id
    for i in new_title_data:
        assert res_data[i] == new_title_data[i]
