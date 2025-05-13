# set : 순서없고 중복 허용안하고,
s1 = {21, 2, 4, 2}
print(len(s1), s1)

raw = [4, 1, 2, 4, 2, 1, 3, 4, 2, 5, 5]
s2 = set(raw)
print(s2)
print(99 in s2)

for v in s2:
    print(v)

s2.add(6)  # 아이템 하나는 이렇게 추가
print(s2)
s2.update(s1)  # 다른 컬렉션의 요소를 현재 set에 추가
print(s2)

# 집합개념이라 이녀석들은 합집합, 교집합, 차집합,
s3 = {1, 2, 6, 8, 9}
s4 = {1, 5, 6, 7}
s5 = s3.union(s4)
print("-----------------------------")
print(s3.union(s4)) # 합   , |
print(s3 | s4)
print("-----------------------------")
print(s3.intersection(s4))  # 교
print(s3 & s4)
print("-----------------------------")
print(s3.difference(s4))    # 차
print(s3 - s4)    # 차
print("-----------------------------")
print(s3.symmetric_difference(s4))    #
print(s3 ^ s4)

arr = [1,4,2,3,4,5,1,3,4]
v =list(set(arr))
print(v)

