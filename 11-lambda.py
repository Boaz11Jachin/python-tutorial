# lambda function : 간단한 기능를 구현하고자 할때 사용할수 있는 함수.
# 람다로 만드는 function 은 작업문을 하나만 가질수 잇다.

def my_multi(a, b):
    return a * b


my_multi2 = lambda a, b: a * b

# def _____ (a) :
#   return a**a

my_pow = lambda a: a ** 2
r = my_pow(17)
print(r)

my_add = lambda a, b: a + b
print(my_add(3, 4))

# 매개변수로 함수를 넘겨야할때가 있는데, 이때 유용하게 활용된다.
data = [1, -3, 4, 55, -2, 1, 4]
data.sort(reverse=True)  # 리스트의 sort는 자신의 값을 이용해서 기본이 오름정렬
print(data)


def custom_sort(v):
    if v > 0:
        return v
    else:
        return -v


# key 라는 인자를 통해 정렬할때 사용할 값을 변경시킬수 있다.
# data.sort(key = custom_sort)
# print(data)

data.sort(key=lambda v: v if v > 0 else -v)
# print(data)

#
skills = ["python", "java", "javascript", "sql"]


def custom_sort(s):
    return len(s)


skills.sort(key=custom_sort, reverse=True)  # 문자열 길이에 따라 sort 되게
skills.sort(reverse=True, key=lambda s: len(s))

print(skills)
