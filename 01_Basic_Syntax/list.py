# 리스트 선언  
my_list = [10, 20, 30]

print(my_list)

element = my_list[2]

print(element)

# Append를 활용한 List 추가 
your_list = [5]
your_list.append(10)
your_list.append(15)
your_list.append(30)

print(your_list)

print(len(my_list))

# Slicing 
sliced = your_list[1:]
print("Sliced : " , sliced)


# in 과 Index를 활용 
fruits = ["banana", "apple", "blueberry", "cherry"]

# 바나나가 포함되어 있는지?
is_banana_included = "banana" in fruits
print("Is banana included?", is_banana_included)

# 체리는 어디에 있는지? 
index_cherry = fruits.index("cherry")
print("cherry is ", index_cherry)

# List의 정렬 
numbers = [4,2,1,3,8,6,7,5]
print("Unsorted", numbers)

# List 숫자 정렬하기 위한 sort()
numbers.sort()
print("Sorted", numbers)

numbers.sort(reverse=True)
print("Sorted (Reverse)", numbers)

# List 요소 추가 및 제거 
my_list2 = []
my_list2.append(10)
my_list2.append(20)
my_list2.append(30)

my_list2.extend([13, 14, 15])

print(my_list2)

# List 연산 (+, *)
new_list = my_list2 + [0, 1, 2]
print(new_list)

multi_lsit = [0, 1, 3] * 3
print(multi_lsit)

# List 연산 (-)
del new_list[0]
print(new_list)

# List 최대값, 최소값 
max_value = max(new_list)
min_value = min(new_list)

print(f"최대 값은 {max_value}, 최소 값은 {min_value}입니다.")