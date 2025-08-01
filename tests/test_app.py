from http import HTTPStatus

from fastapi.testclient import TestClient

from bagual_list.app import app


def test_hello_fastapi():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "hello, fastapi"}
