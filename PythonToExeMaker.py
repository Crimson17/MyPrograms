import easygui, os, ntpath
from shutil import rmtree, copy2

filePath = easygui.fileopenbox("Choose you'r python file.",default=r"C:\Users\Ivan\Documents\GitHub\MyPrograms\*.py")
fileName = ntpath.basename(filePath)
exePath = r"dist\%s.exe" % fileName[:-3]

terminalQuestion = input("Terminal? NO(0) YES(1)")
iconQuestion = input("Icon? NO(0) YES(1)")

os.system("pyinstaller.exe -F %s" % filePath)

rmtree("build")
rmtree("__pycache__")

copy2(exePath, r"C:\Users\Ivan\Desktop\%s.exe" % fileName[:-3])

rmtree("dist")