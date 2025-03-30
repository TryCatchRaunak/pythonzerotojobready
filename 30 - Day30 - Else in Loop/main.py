for i in range(5):
    print(i)

else:#executes after the loop has run from 0 to n-1 
    print("Sorry no i")

for i in []:
    print(i)

else:#here the for loop is empty that's why else executes
    print("Sorry there is no i")



for i in range(6):
    print(i)
    if i==4:
        break

else:#does not execute because the loop was breaked and not completed, thus else after for only executes when the loop has ended or reached it's final value
    print("Sorry no i")



# else can be used with other loops also