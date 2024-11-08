customer = {
    "name": "ashish pal",
    "age": 23,
    "is_verified": True
}

print(type(customer))
print(customer)
print(customer["name"])

customer["birthdate"] = "18 jan 2001"
print(customer["birthdate"])


phone = input("Phone: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch,"!") + " "
print(output)    