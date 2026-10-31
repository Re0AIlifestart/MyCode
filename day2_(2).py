score=80
if score>=75:
    print("优秀")
elif score>=60:
    print("及格")
else:
    print("不及格")

accounts=["admin","root","test","guest"]
for account in accounts:
    print(f"正在测试账号: {account}的登录功能")
    print("测试完成!")

cars_left=5
while cars_left>0:
    print(f"正在查车,还剩{cars_left}辆")
    cars_left-=1
print("查车完成!")

test_cases={
    "id":1,
    "title":"正在登录测试",
    "username":"admin",
    "password":"123456",
    "expected_result":"登录成功"}
print(test_cases["title"])
print(f"登录密码:{test_cases['password']}")

ages=[12,20,22,26,26,28]
for age in ages:
    if age>=18:
        print(f"年龄{age}岁：可以办卡")
    else:
        print(f"年龄{age}岁：不可以办卡")