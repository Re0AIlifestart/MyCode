def check_age(age):
    if age >=18:
        result=f"{age}岁：可以办卡"
    else:
        result=f"{age}岁：不可以办卡"
    return result
print(check_age(12))
print(check_age(20))
print(check_age(65))
ages=[12,20,22,26,26,28]
for age in ages:
    print(check_age(age))

def test_cases(username,password):
    print(f"开始执行登录测试账号，账号:{username}，密码:{password}")
    if username=="admin" and password=="123456":
        result="登录成功"
    else:
        result="登录失败"
    return result
print(test_cases("admin","123456"))
print(test_cases("root","1111111"))

def safe_divide(a,b):
    try :
        result=a/b
        print(f"计算结果是:{result}")
    except ZeroDivisionError:
        print("【报错拦截】:除数不能为0")
print(safe_divide(10,2))

def safe_divide(a,b):
    try :
        result=a/b
        return f"计算结果是:{result}"
    except ZeroDivisionError:
        return "【报错拦截】:除数不能为0"
print(safe_divide(10,2))
print(safe_divide(10,0))


def check_input(input_data):
    try:
        int(input_data)
        return f"输入的是合法数字:{input_data}"
    except ValueError:
        return f"输入的不是纯数字，校验失败!"
for zxc in ["123","abc",50]:
    print(check_input(zxc))