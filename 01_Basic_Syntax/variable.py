import os

# print(os.getcwd())
# print(__file__)


# 변수의 선언
var = 42

# print(var)
# print(var + 10)
# print(var - 5)
# print(var /10)
# print(var // 10)
# print(var % 10)

var2 = var / 10 

print(var > var2)

var_float = 3.14
print(3.14 * 6)
print(3.14 / 2)

result = var * 10 + 5 # 425
# print(result)
result = 5 + var * 10 # 425 
# print(result)
result = (5 + var) * 10 # 475 
print(result)

is_true = True
is_false = False

print(is_true and is_true) # True
print(is_false and is_false) # False
print(is_false and is_false) # False