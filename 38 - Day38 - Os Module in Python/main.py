import os

if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0, 100):
    if(not os.path.exists(f"data/Day{i+1}")):
        os.mkdir(f"data/Day{i+1}")
    else:
        print("Folders already exist!!")