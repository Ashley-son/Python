# 빈 튜플 
my_tuple = (1, )

# 과일 바구니
fruits = ("apple", "banana", "blueberry" )
first = fruits[0]
print("first : ", first)

# 패킹과 언패킹 
tp = 1, 2, 3
print(tp)

v1, v2, v3 = tp
print(f"{v1}, {v2}, {v3}") 

a = 10
b = 20

# temp = a # a = 10, b = 20, temp = 10 
# a = b    # a = 20, b = 20, temp = 10 
# b = temp # a = 20, b = 10, temp = 10  
# 이런식으로 할 필요 없이 언패킹을 통해 간결하게 가능함

a, b = b, a # (20,10) -> 언패킹 예시 
print("a = ", a)

tp2 =  (1, 2, 3, 4, 5, 6, 7, 8)
val1, val2, val3, *vals, _ = tp2
print(vals)

# *vals는 List 형태로 저장되기에 append 등의 연산이 가능함

vals.append(10)
print(vals)

