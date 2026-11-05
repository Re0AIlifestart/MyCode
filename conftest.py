import pytest
import requests
@pytest.fixture
def get_token():
    print("正在登录：获取token")
    url = "https://edgebin.liujiacai.net/post"
    payload = {"username": "admin", "password": "123456"}
    response = requests.post(url, data=payload, timeout=10)
    return "fake_token_123456"