dict = {
    "Raunak": "Mishra",
    "Food": "Chicken",
    "Shoe": "Reebok"
}

print(dict)
print(dict["Raunak"])#This syntax will throw an error if the key doesn't exist
print(dict.get("Raunak"))#This syntax returns None if the key is not present

print(dict.keys())

for key in dict.keys():
    print(f"The corresponding value to key {key} is {dict[key]}")

print(dict.values())


print(dict.items())
for key, value in dict.items():
    print(f"The corresponding value to the key {key} is {value}")