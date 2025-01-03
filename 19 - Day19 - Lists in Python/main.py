marks = [3,4,5,6]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
for mark in marks:
    print(mark)



list1 = ['raunak', 'raj', 44, 24, True]
print(list1)
print(type(list1))

#Negative indexing
print(list1[-3])
print(list1[4-3])


print(list1[1:3])


if True in list1:
    print('yes')
else:
    print('no')

#Same thing applies for strings as well
if 'nak' in 'raunak':
    print('yes')
else:
    print('no')



lst = [i for i in range(21)]
print(lst)
lst = [i*i for i in range(21)]
print(lst)