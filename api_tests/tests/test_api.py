import pytest
import allure
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import APIConfig
from services.api_client import APIClient


@allure.feature("API Тестирование apimocker.com")
class TestAPI:

    def setup_method(self):
        self.client = APIClient(APIConfig.BASE_URL)

    @allure.title("GET запрос - получение постов")
    def test_get_posts(self):
        response = self.client.get(APIConfig.ENDPOINTS["posts"])
        assert response.status_code == 200
        # apimocker.com возвращает {data: [...], pagination: {...}}
        data = response.json()
        assert "data" in data
        assert isinstance(data["data"], list)
        print("✅ GET /posts работает")

    @allure.title("GET запрос - получение конкретного поста")
    def test_get_post_by_id(self):
        response = self.client.get(f"{APIConfig.ENDPOINTS['posts']}/1")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert "id" in data["data"]
        print("✅ GET /posts/1 работает")

    @allure.title("POST запрос - создание поста")
    def test_create_post(self):
        new_post = {"title": "Test Post", "body": "Test body", "userId": 1}
        response = self.client.post(APIConfig.ENDPOINTS["posts"], data=new_post)
        # apimocker.com возвращает 200, а не 201
        assert response.status_code in [200, 201]
        data = response.json()
        assert "data" in data
        print("✅ POST /posts работает")

    @allure.title("GET запрос - получение пользователей")
    def test_get_users(self):
        response = self.client.get(APIConfig.ENDPOINTS["users"])
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert isinstance(data["data"], list)
        print("✅ GET /users работает")

    @allure.title("GET запрос - получение комментариев")
    def test_get_comments(self):
        response = self.client.get(APIConfig.ENDPOINTS["comments"], params={"_limit": 5})
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        print("✅ GET /comments работает")