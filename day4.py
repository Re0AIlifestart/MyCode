import requests
url="https://httpbin.org/get"
response=requests.get(url)
print("状态码",response.status_code)
print("响应内容",response.text)
url="https://httpbin.org/ip"
response=requests.get(url)
data=response.json()
print("转换后的数据类型:",type(data))
print("提取其中的ip字段：",data["origin"])

import requests
def test_login():
    url="https://httpbin.org/post"
    payload={"username":"admin","password":"123456"}
    response=requests.post(url,data=payload)
    if response.status_code==200:
        print("测试通过：接口返回 200")
        res_data=response.json()
        if res_data["form"]["username"]=="admin" and res_data["form"]["password"]=="123456":
            print("测试通过：账号数据提交成功！")
    else:
        print(f"测试失败：接口报错，状态码{response.status_code}")
test_login()
