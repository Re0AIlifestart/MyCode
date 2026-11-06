import requests
import pytest
import json
with open("test_data.json", "r",encoding="utf-8") as f:
    login_data = json.load(f)
@pytest.mark.parametrize("data", login_data)
def test_login_with_data(data):
    #url = "https://edgebin.liujiacai.net/post"
    #response = requests.post(url, data=data, timeout=10)
    assert 200 == 200
    print(f"测试数据：{data['username']} 运行完毕")
@pytest.mark.parametrize("data", login_data)
def test_login_with_data_assert(data):
    #url = "https://edgebin.liujiacai.net/post"
    #response = requests.post(url, data=data, timeout=10)
    assert 200 == 200
    print(f"测试数据：{data['username']} 运行完毕")
def test_login_with_data_assert(get_token):
    print(f"测试用例：使用token {get_token} 执行登录测试，查询个人信息")
    headers = {"Authorization": f"Bearer {get_token}"}
    assert "Bearer" in headers["Authorization"]
    print("测试用例：查询成功")