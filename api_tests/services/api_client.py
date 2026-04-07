import requests
import allure


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    @allure.step("GET запрос к {endpoint}")
    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params)
        allure.attach(str(response.status_code), name="Status code", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text[:500], name="Response body", attachment_type=allure.attachment_type.TEXT)
        return response

    @allure.step("POST запрос к {endpoint}")
    def post(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, json=data)
        allure.attach(str(response.status_code), name="Status code", attachment_type=allure.attachment_type.TEXT)
        return response

    @allure.step("PUT запрос к {endpoint}")
    def put(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, json=data)
        return response

    @allure.step("DELETE запрос к {endpoint}")
    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url)
        return response