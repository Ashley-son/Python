# 문자열 변수 선업
str_var = "This is my python code."
# multi_line = """I'm a developer.
# I use python.
# Thank you."""

print(str_var.upper())
print(str_var.swapcase())
print(str_var.replace("my","your"))

# print(str_var)
# print(multi_line)

# 문자열 더하기 

# 인덱싱
# print(str_var[11])


# 슬라이싱 
print(str_var[11:17])

# isalpha는 영어인지 확인하는 용도 
# isdecimal은 숫자인지 확인하는 용도 


# Format String
weather = "흐림"
temp = 15.9

# %code
print("오늘 날씨는 %s 입니다. 기온은 %f 입니다." % (weather, temp))

# .format()
res = "오늘 날씨는 {} 입니다. 기온은 {} 입니다.".format(weather, temp)
print(res)

# f""
res1 = f"오늘 날씨는 {weather}입니다. 기온은 {temp}입니다."
print(res1)

# 사용자로부터 문자열 입력 받기
# print("숫자를 입력해주세요")
# num = input()
# print(num)

# 이값을 1더해서 출력하기 
inp = input("값을 입력해주세요.")
num = int(inp) + 1
print(f"입력 받은 값에 1을 더하면, {num} 입니다.")

# input()함수는 사용자로부터 값을 입력받기 위하여 사용함
# 일반적으로는 문자열로 입력 받기에 숫자로 받기 위해선 정수형으로 변환 