# 함수 : 특정 역할을 수행하기 위한 코드묶음
# 파이선에서 함수 만들기 : def 라는 키워드를 이용해서 function을 정의
def test() :
    print("test function called")

test()
# test(4)   # 매개변수 개수 안맞으면 error 

def add(n1, n2) :
    return n1 + n2

r = add(4, 5)
print(r)


# function define 할때 매개변수 기본값 설정 가능
def greet(name="anonymous") :
    print(f"Hello? {name}~")

greet("luffy")
greet()   # 매개변수 개수 안맞으면 error






