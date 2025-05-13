# python의 if statement
from os import fdopen

fee = 1000
age = int(input("Your age? "))
# print(type(a))
if age > 17:
    print("20% additional charge occur")
    fee *= 1.2
elif age < 6:
    print("30% discounted")
    fee *= 0.7
else:
    print("welcome")

print(f"your ticket price is {fee}")






