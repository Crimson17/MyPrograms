from shutil import copy2
import os, time, requests

num = 0
while os.path.isdir(r"C:\Users\Ivan\Desktop\Reaper_Project_%d" % num) == True:
    num=num+1
os.mkdir(r"C:\Users\Ivan\Desktop\Reaper_Project_%d" % num)
time.sleep(1)
copy2(r"C:\Users\Ivan\Dropbox\DefaultFile\Default.rpp", r"C:\Users\Ivan\Desktop\Reaper_Project_%d" % num)
os.rename(r"C:\Users\Ivan\Desktop\Reaper_Project_%d\Default.rpp" % num, r"C:\Users\Ivan\Desktop\Reaper_Project_%d\Reaper_Project.rpp" % num)
file = open(r"C:\Users\Ivan\Desktop\Reaper_Project_%d\Enjoy_Your_Recording.txt" % num,"w+")
file.write("Good luck and have fun!")