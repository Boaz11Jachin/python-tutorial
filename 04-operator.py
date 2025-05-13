# comparison operator 비교 연산
# == , !=, >, <, >=, <=
print(4 == 4)
print("김병재" > "고민석")
print('Apple' == 'Apple')
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)

# logical operator 논리연산
# and(&&), or(||) , not (!)
x, y = 14, 19
result = (x > 0 and y > 0)
print(result)
print(x >= 0 and x <= 20)
print(0 <= x <= 20)

# membership operator
# in : 포함되었다면 True, not in : 포함되어있지 않다면 True
print()
print('java' in 'javascript')
print(1 in [11, 2, 3, 4, 5, 1])

# identity operator : 객체 동등성 체크   . is   is not
print()
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)
print(a is b)

# 3항연산  ?    :
num = 4
# r = num %2 ==0 ? "even" : "odd"
r = "even" if num % 2 == 0 else "odd" 
print(r)
