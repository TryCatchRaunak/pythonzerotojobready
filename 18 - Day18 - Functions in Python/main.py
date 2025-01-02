def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if(a>b):
        print(a, 'is greater than', b)
    else:
        print(b, 'is greater than', a)

a = 9
b = 8
calculateGmean(a, b)
isGreater(a, b)

c = 7
d = 4
calculateGmean(c, d)
isGreater(c, d)