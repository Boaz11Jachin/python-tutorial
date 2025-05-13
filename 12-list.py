# list : 타 언어의 배열같은 느낌의 컬렉션 (파이썬에는 list 외에 tuple, set, dictionary 도 있다)
#
my_list = ["luffy", "zoro", "nami", "sanji","chopper","franky"]
print(len(my_list))
my_list2 = []
my_list3 = list()
print(my_list2, my_list3)
my_list4 = list({"fire", "water", "earth"})
print(my_list4)

# access items
print(my_list[0])
print(my_list[-3])  # negative indexing 은 끝에서부터 위치

# slicing
print(my_list[2:])
print(my_list[:5])
print(my_list[3:5])
print(my_list[-5:-3])
print(my_list[:])

# present check
print("ace" in my_list)

# add item
my_list.append("robin")
print(my_list)

my_list.extend(my_list4)    # another list
print(my_list)
my_list += my_list4 # extends 는 += 로도 가능
print(my_list)
# my_list += "ace"
print(my_list)










