import requests

stranica = input("Url straince: ")
site = requests.get(stranica)

file = open("SiteData.txt","w+")
file.write("")
file.write(site.text)
