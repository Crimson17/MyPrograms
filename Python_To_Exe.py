import easygui, os, ntpath, sys, time
from shutil import rmtree, copy2

filePath = easygui.fileopenbox("Choose your python file.", default=r"C:\Users\Ivan\Documents\GitHub\MyPrograms\*.py")
fileName = ntpath.basename(filePath)
exePath = r"dist\%s.exe" % fileName[:-3]
commandString = "pyinstaller.exe -F"

terminalQuestion = easygui.buttonbox("Terminal?", "Choose one:", ('Yes', 'No'),)
iconQuestion = easygui.buttonbox("Icon?", "Choose one:", ('Yes', 'No'),)

pycachePath = filePath[:-len(fileName)] + "__pycache__"

if terminalQuestion == "No":
    commandString = commandString + " -w"

if iconQuestion == "Yes":
    icoFilePath = easygui.fileopenbox("Choose your icon file.")
    if ".ico" not in ntpath.basename(icoFilePath):
        print("Icon file must have .ico extension")
        time.sleep(4)
        sys.exit()
    commandString = commandString + " -i " + icoFilePath
time.sleep(0.1)

os.system(commandString + " " + filePath)
time.sleep(0.1)

if os.path.isdir("build"):
    rmtree("build")
    print("build deleted")
time.sleep(0.1)

if os.path.isdir(pycachePath):
    rmtree(pycachePath)
    print("__pycache__ deleted")
time.sleep(0.1)

copy2(exePath, r"C:\Users\Ivan\Desktop\%s.exe" % fileName[:-3])
print("Exe copied to desktop")
time.sleep(0.1)

if os.path.isdir("dist"):
    rmtree("dist")
    print("dist deleted")

if os.path.exists(fileName[:-3] + ".spec"):
    os.remove(fileName[:-3] + ".spec")
    print(fileName[:-3] + ".spec" + " deleted")
print("Job finished!")
