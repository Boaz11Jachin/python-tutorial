
# dictionary : 키-값 형태로 되어있는 컬렉션,
car = {
    "brand" : "kia",
    "model" : "sorrento",
    "price" : 3500
}

print(type(car))
movie = dict(title="Mine-craft", realease =2025)
print(type(movie))
print(car, movie)

print(len(car), len(movie) )

print( "brand" in car, "kia" in car)

for x in car :
    print(x, car[x])

print(car["brand"])

print(car.values())
for v in car.values() :
    print(v)

print(car.items())

for key, value in car.items() :
    print(key, value)

del car["brand"]
print(car.keys())
car["price"] = 4000
print(car)
car["rating"] = 9.2
print(car)
car.update({"rating" : 9.1, "promotion" :  True})
print(car)

car["Promotion"] = car["promotion"]
print(car)
del car["promotion"]




















