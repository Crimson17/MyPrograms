

webpage = ("https://www.bloomberg.com/quote/SPX:IND")
pagehtml = urllib.urlopen(webpage)
soup = BeautifulSoup(pagehtml, "html.parser")
name_box = soup.find("h1", attrs={"class":"name"})
name = name_box.text.strip()
print(name)