import requests

stranica = input("Url straince: ")
site = requests.get(stranica)

file = open(r"C:\Users\Ivan\Desktop\SiteData.txt","w+")
file.write("")
file.write(site.text)
