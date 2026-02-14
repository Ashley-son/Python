# 비어있는, 간단한 딕셔너리 만들기 
my_dict = {}
my_dict["key"] = "value"
print(my_dict)

# 복잡 딕셔너리 
person = {"name": "홍길동", "age": "30", "city": "서울"}
person["age"] = 35 # value 값을 변경한 경우
name = person["name"]

person_detail = {"country" : "대한민국", "married" : True}

# update 함수 이용
person.update(person_detail)

print(name)

print(f"이름은 {person['name']}, 나이는 {person['age']}, 고향은 {person['city']} 입니다.")

# key error가 발생한 경우
# country = person["country"]
# print(f"국적은 {country} 입니다.")

# key값이 없을 경우 get 함수 이용 하여 기본 값 사용
country = person.get("country", "알 수 없음")
print(f"국적은 {country} 입니다.")

# person의 keys 불러오기 
print(person.keys())

# 불필요한 key 삭제하기 
del person["married"]
print(person.keys())