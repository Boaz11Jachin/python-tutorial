# variable : 변수
# 파이썬에서 변수는 별도 과정이 필요하지 않고, 할당하는 순간 만들어짐
x = 5
y = "python"

print(x)
print(y)
print(x, y)

# 변수 사용할때 특정한 자료형이 필요하지 않고, 자료형이 언제든 바뀐다.
print(x, type(x))
x = 3234.2
print(x, type(x))

# 변수명은 파이썬은 보통 스네이크 케이스로 작명함.
number_of_student = 12

# 파이썬에서는 변수 여러개를 동시 선언하며 값을 설정할수 있다
kor, eng, math = 100, 30, 79
print(kor, eng, math)

subjects = ["java", 'python', "javascript"] # 문자열 쌍따옴표, 홀따옴표 둘다 됨
print(type(subjects))

# list 같은 컬렉션들은 바로 추출도 가능
x, y, z = subjects
print(x)
print(y)
print(z)
