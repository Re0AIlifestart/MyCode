import pytest
import requests
@pytest.fixture
def get_token():
    print("正在登录：获取token")
    token = "fake_token_123456" 
    yield token
    print("测试结束：清理资源")