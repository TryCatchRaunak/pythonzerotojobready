x = int(input("Enter the value of x: "))

#Match case statements
match x:
    case 0:
        print("X is zero")
    case 5:
        print("X is five")
    case _ if x!=90:
        print(x, "is not 90")
    case _:
        print("X is < 10")