# string : 문자열 , 홀따옴표, 혹은 쌍따옴표로 묶어서 표기
a = "python"
b = 'python'

# 문자열 길이 는 len 이라는 built-in function 을 이용
print(len(a))
arr = [1, 4, 54, 36, 435, 324, 424, 235, 432, 5432, 5432]
print(len(arr))  # len 함수는 나중에 컬렉션 유형에도 사용가능

# 내부적으로는 문자들의 집합형태로 관리되는 list 구조이기 때문에 slicing
x = a[2:5]  # position 2 ->  5(5 는 not include)
print(x)
print(arr[1: 4])
print(a[:4], a[2:])

# string concat
print("Hello," +" Python")
a += "! Nice to meet you"
print(a)

# 일반 프로그래밍 언어랑 비슷하게 string 가지고 했던 작업들 다 메서드로 존재함.
# string modify method
a  = "Hello,Python"
print(a.upper())
print(a.lower())
print(a.replace("Python","Java"))
print(a.split(","), type(a.split(",")) )


