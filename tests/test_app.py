
from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_health_check():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_quiz_submission():
    client = app.test_client()

    answers = {
        "question0": "Central Processing Unit",
        "question1": "All of these",
        "question2": "Create containers",
        "question3": "Jenkins",
        "question4": "Containers"
    }

    response = client.post("/submit", data=answers)

    assert response.status_code == 200
    assert b"5 / 5" in response.data
