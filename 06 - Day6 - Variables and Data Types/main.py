#Python does not require users to specify the data types of variables

a = 122312312
print(a)
b = "raunak"
print(b)


# print(a + b)
#    print(a + b)
#           ~~^~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(a , b)

print(type(a))
print(type(b))


list1 = [8, 2.3, [-4,5], ["apple", "banana"]]
print(list1)

#There is only one difference between list and tuple - Tuple is immutable

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)


dict1 = {"name":"Rajeev", "age":34, "canVote":True}
print(dict1)