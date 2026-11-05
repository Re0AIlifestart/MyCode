import pytest
@pytest.fixture
def prepare_data():
    print("准备测试数据")
    data={"username":"admin","password":"123456"}
    return data
def test_login_(prepare_data):
    print(f"登录测试: {prepare_data['username']}")
    assert prepare_data["username"]=="admin"

def test_get_user_info(get_token):
    print(f"执行用户信息测试:使用 {get_token}请求用户信息")
    assert get_token=="fake_token_123456"