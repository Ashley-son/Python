# 함수의 기초 
def func(name):
    print(f"This is Function. Hello{name}!")

func("Park")

# 반환값을 이용한 함수 호출 
def sum(num1, num2):
    return num1 + num2

def div(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1 / num2

result = sum(3, 5)
result_div = div(3,2)
print(result)
print(result_div)