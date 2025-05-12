import os 

# for i in range(0, 100):
#     os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}")
# print("Successfully Renamed all the files")

folders = os.listdir("data")
print(folders)