# 비어있는 set 만들기
empty_set = set()
# 기본적으로 비어있는 {}는 딕셔너리로 정의되기에 비어있는 set을 만들기 위해서는 set()으로 할당 

my_set = {1, 2, 2, 3}

print(my_set)

#set 정의하기 
fruits = {"apple", "banana", "blueberry"}
print(fruits)

fruits.add("orange")
print(fruits)
# set은 순서를 보장하지 않음 

fruits.remove("banana")
print(fruits)


fruits1 = {"apple", "strawberry", "peach"}
fruits2 = {"banana", "strawberry", "orange"}

# 합집합
union = fruits1.union(fruits2)
print(union)
print(fruits1 | fruits2)

# 교집합
intersection = fruits1.intersection(fruits2)
print(intersection)
print(fruits1 & fruits2)

# 차집함 (순서 중요)
diff1 = fruits1.difference(fruits2)
diff2 = fruits2.difference(fruits1)
diff3 = fruits1 - fruits2

print(diff1)
print(diff2)
print(diff1-diff2)
print(diff3)