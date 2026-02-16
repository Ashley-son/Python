# 단일 조건 조건문 
# 이 값이 20을 초과하는 경우, Big! 이라는 메시지를 출력 
value = 30

if value > 20 :
    print("Big!")

# 복합 조건문
# 50보다 큰 경우 Great, 20보다 큰 경우 Big, 그렇지 않은 경우 Small
value2 = 50

if value2 > 50:
    print("Great!")
elif value2 <= 50 and value2 > 20 :
    print("Big!")
else:
    print("Small!")

# 날씨가 흐리고, 강수 확률이 70% 이상이면 비가 온다. 

condition = "맑음"
rain_rate = 0.70

if condition is "흐림" and rain_rate >=0.70:
    print("비가 올 확률이 높습니다.")
elif condition is "흐림":
    print("날씨가 많이 흐립니다.")
elif condition is "맑음" and rain_rate >= 0.70:
    print("맑지만 비가 올 확률이 높습니다.")
else:
    print("날씨가 좋습니다.")

# 사용자로부터 두 개의 값을 입력받는다.
var1 = input("첫 번째 값을 입력해주세요 : ")
var2 = input("두 번째 값을 입력해주세요 : ")

# 입력값을 숫자로 변환 
num_var1 = int(var1)
num_var2 = int(var2)

# 첫 번째 값이 크다면 "Win", 두 번째 값이 크다면 "Lose"를 출력한다.
# 두 값이 같다면, "Draw"를 출력한다.
if num_var1 > num_var2:
    print("Win")

elif num_var1 < num_var2:
    print("Lose")

else:
    print("Draw")