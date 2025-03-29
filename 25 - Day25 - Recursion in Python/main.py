def factorial(num):
    if (num==0 or num==1):
        return 1
    else:
        return num*factorial(num-1)

print(factorial(7))


def fibonacci(range):
    if(range==1):
        return 0
    elif(range==2):
        return 1
    elif(range>2):
        return fibonacci(range-1) + fibonacci(range-2)

print(fibonacci(12))