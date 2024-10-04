# Strings are immutable
a = "!!Raunak!!! Raunak!!!! ~~~Raunak"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))#trims the trailing exclamation marks and not the leading ones
print(a.replace("Raunak", "mishra"))
print(a.split(" "))

blogHeading = "this is my first Blog"
print(blogHeading.capitalize())#Capitalises the first letter of the string and also converts any other letter into lowerCase if present

console = "Welcome to the console!!!"
print(console.center(50))

print(a.count("Raunak"))#Counts the occurence of a particular element in a string
print(console.endswith("!!!"))
print(console.endswith("to", 4, 10))

print(console.find("the"))#returns -1 if nothing found
# print(console.index("isshh"))#gives error if element not found

print(console.isalnum())#returns true for string containing A-Z, a-z, 0-9
print(console.isalpha())#returns true for string containing A-Z, a-z

cap = "RAUNAK"
print(cap.islower())

print(cap.isprintable())#\n \t etc. are non-printable characters
print(console.isspace())#return true if string is " "

print(blogHeading.istitle())

str1 = "Python is my favourite language"
print(str1.startswith("Python"))
print(str1.swapcase())

print(str1.title())