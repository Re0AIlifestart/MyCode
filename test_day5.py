def test_basic_sasert():
    expected=100
    actual=50+50
    assert actual==expected
def test_fail_example():
    assert 1==1
import requests
def test_login():
    url="https://httpbin.org/post"
    payload={"username":"admin","password":"123456"}
    response=requests.post(url,data=payload)
    assert response.status_code==200
    res_data=response.json()
    assert res_data["form"]["username"]=="admin" and res_data["form"]["password"]=="123456"
  
import pytest
test_data=[("admin","123456"),("root","123456"),("admin","888888")]
@pytest.mark.parametrize("user,pwd",test_data)
def test_multi_login(user,pwd):
    url="https://httpbin.org/post"
    payload={"username":user,"password":pwd}
    response=requests.post(url,data=payload)
    assert response.status_code==200
    print(f"账号:{user},密码:{pwd},测试完成")