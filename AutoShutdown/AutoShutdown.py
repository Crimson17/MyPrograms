import os

print("Input the amount of time before shutdown.")
print("If you want to remove the schedule type 0 in hours and 0 in minutes!")
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))

timeInSeconds = (hours*3600) + (minutes*60)
if timeInSeconds == 0:
    command = "shutdown /a"
else:
    command = "shutdown -s -t %d" % timeInSeconds

os.system(command)
