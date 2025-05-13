# 파이썬에서 사용하는 기본 데이터 타입
a = "pyton"
print(a, type(a))
b = 432
print(b, type(b))
c = 3.324
print(c, type(c))
d = 4j
print(d, type(d))
e = True  # False
print(e, type(e))

# 컬렉션 (데이터 집합체)
aa = ["apple", "banana", "cherry"]
print(aa, type(aa))
print(aa[0])
aa[0] = "Apple"

bb = ("apple", "banana", "cherry")
print(bb, type(bb))
print(bb[0])
# bb[0] = "Apple"

cc = {"apple", "banana", "cherry" , "apple"}
print(cc, type(cc))
# print(cc[0])

dd = {"name" : "luffy", "age" :  19}
print(dd, type(dd))
# print(dd.name)
print(dd["name"])