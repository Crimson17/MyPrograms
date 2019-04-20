import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.random.org/")
soup = BeautifulSoup(r.text, "html.parser")
print(soup)