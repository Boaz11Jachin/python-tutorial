# for loop : 다른언어의 일반 for 보다는 for-each 에 가까운 for문
# 열거형 순회하는 용도의 for 문
names = ["luffy", "zoro", "sanji", "nami", "usop"]
for n in names :
    if n =="sanji" :
        break
    print(n)


print("-------------------------------------")

txt = "programming"
for x in txt:
    print(x)

# 일반 for문 형태로 사용하고 싶다면 range() function ==> number sequence 만들때 사용
print(range(5)) # [0,1,2,3,4]
print( type( range(4) ) )

# range 매개변수를 하나만 쓰면, 0부터 숫자가 1씩 증가되면서  나옴 (끝값 not include)
#                 두개를 쓰면, 특정 시작값,   세개를 쓰면 step (증가량)
for x in range(3, 10, 2) :
    print(x)

for _ in range(10) :
    print("python")