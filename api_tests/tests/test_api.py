import pytest
import allure
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@allure.feature("API Тестирование")
class TestAPI:

    @allure.title("GET /posts")
    def test_get_posts(self):
        response = requests.get(f"{BASE_URL}/posts")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        print("GET /posts работает")

    @allure.title("GET /posts/1")
    def test_get_post_by_id(self):
        response = requests.get(f"{BASE_URL}/posts/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1
        print("GET /posts/1 работает")

    @allure.title("POST /posts")
    def test_create_post(self):
        data = {"title": "Test Post", "body": "Test body", "userId": 1}
        response = requests.post(f"{BASE_URL}/posts", json=data)
        assert response.status_code == 201
        assert response.json()["title"] == "Test Post"
        print("POST /posts работает")

    @allure.title("GET /users")
    def test_get_users(self):
        response = requests.get(f"{BASE_URL}/users")
        assert response.status_code == 200
        assert len(response.json()) > 0
        print("GET /users работает")

    @allure.title("GET /comments")
    def test_get_comments(self):
        response = requests.get(f"{BASE_URL}/comments", params={"_limit": 5})
        assert response.status_code == 200
        print("GET /comments работает")