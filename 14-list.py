import random

my_list = ["luffy", "zoro", "nami", "sanji","chopper","franky"]

# loop
for x in my_list:
    print(x)

print(len(my_list))

for i in range(len(my_list)) :
    print(i , my_list[i])

my_number = [145, 4,2, 5, 14, 5, 52, 1, 5]
# 짝수만 가진 배열을 만들고,   배열에서 filter
even_number = []
for n in my_number :
    if n % 2 == 0 :
        even_number.append(n)
# 현재 기본 값을 2배한 배열을 만들  배열에서 map
double_number = []
for n in my_number :
    double_number.append(n * 2)

print(even_number)
print(double_number)

# 기존 배열을 토대로 이런 작업들을 간단하게 할수 있는 문법이 있음
# list comprehension
copy_number=[ print(n) for n in my_number ]
print(copy_number)

copy_number=[ n for n in my_number ]
print(copy_number)
double_number_2 = [  n*2  for n in my_number]
print(double_number == double_number_2)
even_number_2 = [ n for n in my_number if n%2 == 0]
print(even_number == even_number_2)

arr =[ random.randint(10, 100)  for n in range(1, 11)]
print(arr)

def test() :
    print("test")

r = test()
print(r)






