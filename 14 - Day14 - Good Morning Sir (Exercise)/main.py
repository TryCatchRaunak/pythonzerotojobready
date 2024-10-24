import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)


if(timestamp >= '04:00:00' and timestamp <= '11:00:00'):
    print("Good Morning sir!!")
elif(timestamp >= '11:00:01' and timestamp <= '16:00:00'):
    print("Good Afternoon sir!!")
elif(timestamp >= '16:00:01' and timestamp <= '22:00:00'):
    print("Good Evening sir!!")
else:
    print("Good Night sir!!")