data = [
    {"name": "윤형호", "age": 19},
    {"name": "김병재", "age": 29},
    {"name": "문진수", "age": 27}
]

# data = ["banana", "apple", "apple-mango", "cherry"]
# print(data[0]["name"] > data[1]["name"])

print(data)
def convert_to_age (item) :
    return item["age"]

print(convert_to_age(data[0]))

# data.sort(key=convert_to_age)
data.sort(key = lambda item : item["name"])

print(data)