a = input("Enter the number: ")
print(f"Multiplication Table of {a} is: ")
try:
    for i in range(1, 13):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("Some important lines of code")
print("Executed")


try:
    num=int(input("Enter an integer"))
    b=[6,3]
    print(b[num])
except ValueError:#Handling specific errors
    print("The number entered is not an integer")
except IndexError:
    print("Index error")