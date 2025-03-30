marks = [12, 56, 32, 98, 12, 45, 1, 4]

# for mark in marks:
#     print(mark)
#     if(index == 3):#this would throw an error because index variable is not defined
#         print("Raunak is awesome!")

#Therefore we have to write it like this
# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Raunak is awesome!")
#     index += 1


#But there is a much better way to do this
for index, mark in enumerate(marks):#Here the enumerate function sets the sequence in a list, tuple or string
    print(mark)
    if(index == 3):
        print("Raunak is awesome!")


#By default enumerate starts from 0 but there is a use case where we can specify a starting index
for index, mark in enumerate(marks, start=2):
    print(mark)
    if(index == 2):
        print("SEEING...")