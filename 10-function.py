def guess_quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x > 0 and y < 0:
        return 4
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 0


# 매개변수를 넘길때, position 을 이용해서 넘길때, keyword를 이용해서 넘기는 방법도 있다.
a = guess_quadrant(4, 2)
b = guess_quadrant(x=-4, y=7)  # 매개변수 순서를 안지켜도 됨
c = guess_quadrant(y=10, x=1)
print(a, b, c)
# d = guess_quadrant(-3, x =4)
# 특정함수를 쓰다보면 매개변수 꽤많은 애들이 있는데, 
# 그런 함수들은 매개변수부분에 defaultValue 들을 처리해두는 경우가 많아서
# 특정인자만 전달하고자 할때 보통 사용을 한다

def dutch_pay(price=0, already=0, person=0, equal=True) :
    current = price - already
    if equal :
        return current / person
    else :
        return current // person

r = dutch_pay(10000, 2000, 3, True)
print(r)

r = dutch_pay(13000, person= 3) # dutch_pay(13000, person=3)
print(r)
r = dutch_pay(13000, 0, 3)

print(type(dutch_pay))

dp = dutch_pay  # 파이썬에서도 function 이 매개변수 전달되는 경우도 있을꺼다.
print(dp(13000, person=2))




