tup = (1,4,5)
print(type(tup), tup)

tup1 = (2,)#if we are including only a single element in a tuple then we have to keep a comma at the end for the interpreter to understand it is a tuple

#TUPLE IS USED WHEN IN A VERY COMPLEX PROGRAM WE DO NOT WANT TO CHANGE THE ITEMS 
#OTHERWISE WE COULD HAVE USED LIST

tup2 = (1,3,4,5,6,"red",True)
print(type(tup2), tup2)
print(tup2[0])
print(tup2[1])
print(tup2[2])
print(tup2[3])
print(tup2[4])
print(tup2[5])
print(tup2[6])

tup3 = tup2[1:5]
print(tup3)