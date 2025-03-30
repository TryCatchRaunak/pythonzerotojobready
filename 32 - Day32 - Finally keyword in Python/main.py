try:
    l = [1,5,6,8]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occurred")
finally:
    a = 3
    b = 4
    print(a+b)

# Now we would think that what is the need of finally keyword
# when alread we can do it somewhat like this 

# try:
#     print("run")
# except:
#     print("error")

# print("Always runs")

# This block would also run and do the same task as the previous
# block which uses finally keyword.
# So what is the difference ?

#The difference arises when we use these blocks in a function/method
def function():
    try:
        number = int(input("Enter a number"))
        print(number)
    except:
        print("Some error occurred")
    finally:
        print("I am always executed")

function()


# Would we have not used finally keyword the code under finally section 
# have never executed