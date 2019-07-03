import easygui, os
from shutil import copy2
import PyInstaller

y = "0"
o = str('\\')
pathList = []
listNameOfTheFile = []
nameOfTheFile = ""


filePath = easygui.fileopenbox("Choose you'r python file.",default=r"C:\Users\Ivan\Documents\GitHub\MyPrograms\*.py")
desktopFolderPath = r"C:\Users\Ivan\Desktop\ExeMakerFolder"

for x in filePath:
    pathList.insert(0,str(x))
for y in pathList:
    if y == o:
        break
    else:
        listNameOfTheFile.insert(0,y)
for z in listNameOfTheFile:
    nameOfTheFile = nameOfTheFile + z

if not os.path.exists(desktopFolderPath):
    os.mkdir(desktopFolderPath, 0o777)
copy2(filePath, desktopFolderPath + "\\" + nameOfTheFile)

pathToTheFile = desktopFolderPath + "\\" + nameOfTheFile
print(nameOfTheFile)
print(pathToTheFile)


os.system(r"cd C:\Users\Ivan\Desktop\ExeMakerFolder")
os.system("pyinstaller -F %s" % pathToTheFile)


