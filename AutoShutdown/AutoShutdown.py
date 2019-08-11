import os

print("Input the amount of time before shutdown.")
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))

timeInSeconds = (hours*3600) + (minutes*60)
command = "shutdown -s -t %d" % timeInSeconds

os.system(command)
