applePrice = int(input("Enter the price of apples: "))
budget = 200
if(budget - applePrice>50):
    print("Alexa, add 1kg apples to the cart.")
elif(budget - applePrice>70):
    print("Its okay you can buy")
else:
    print("Alexa, do not add apples to the cart.")