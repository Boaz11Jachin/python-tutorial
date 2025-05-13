
# tuple : list(순서가 있음)와 비슷하긴 한데 값 변경은 불가 (고정 list)
# 만들때 ( 로  ,  [는 list
t1 = ("fire", "water", "earth", "wind", "fire")
print(t1)
print(t1[0])
print(len(t1))
# t1[0] = "Fire"
for v in t1 :
    print(v)

t2 = ("light", "dark")
t3 = t1 + t2
print(t3)
print( "fire" in t2)