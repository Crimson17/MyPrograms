import os, easygui
from zipfile import ZipFile

i = 0
allFilesList = []

directoryPath = easygui.diropenbox("Choose a folder where files are located: ")

for r, d, f in os.walk(directoryPath):
    for file in f:
        allFilesList.append(os.path.join(r, file))

with ZipFile(os.path.join(directoryPath, 'zipiran.cbr'), 'w') as zip:
    for x in allFilesList:
        z = "%02d.jpg" % i
        y = os.path.join(directoryPath, z)
        os.rename(x, y)
        i = i + 1
        zip.write(y, arcname=z)
