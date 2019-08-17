import os

path = r"C:\Users\Ivan\Desktop\DS3_Bosses"

files = []
listOfEditedNames = []

for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

for f in files:
    oldFilePath = f
    listOfNameChars = []
    listOfChars = list(f)
    for x in listOfChars:
        if x == "_" or x == "-" or x == ",":
            listOfChars.remove(x)
    for z in reversed(listOfChars):
        if z != "\\":
            listOfNameChars.insert(0, z)
        else:
            break
    pureFileNames = ''.join(listOfNameChars).lower()
    f = r"C:\Users\Ivan\Desktop\DS3_Bosses" + "\\" + pureFileNames
    os.rename(oldFilePath, f)
