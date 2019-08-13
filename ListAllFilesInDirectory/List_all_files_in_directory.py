import os

directoryPath = input("Input your directory path here: ")

filesList = os.listdir(directoryPath)

for i in filesList:
    print(i)
