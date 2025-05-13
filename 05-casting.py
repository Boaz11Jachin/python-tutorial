import random

# 이 데이터를 시간과 분으로 나눠서 출력
total_minute = random.randint(60, 240)
print(total_minute)

hour = total_minute // 60
minute = total_minute % 60
print(hour, minute)
# XXX분은 X시간 X분 입니다.
# print(total_minute+" minute is " + hour +"h " + minute+"min ")

# casting : 데이터 유형을 원하는 형태로 변경하고자 할때 사용
# int() , float(), str(),  bool()
print(int(4.92), int("43"))
print(float(4), float("43.43"))
print(str(4), str(45.22))
print(bool(1), bool("True"), bool(""))

print(str(total_minute) + " minute is " + str(hour) + "h " + str(minute) + "min ")

txt = f"{total_minute} minutes is {hour:02d} h, {minute:02d} min."  # format string
print(txt)

