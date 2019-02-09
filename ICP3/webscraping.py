import urllib.request
from bs4 import BeautifulSoup

wikiURL = "https://en.wikipedia.org/wiki/Deep_learning"
fpURL = urllib.request.urlopen(wikiURL)


soup = BeautifulSoup(fpURL, "html.parser")


title = soup.find('title')
print("Title --> ", title.text)


links = soup.find_all('a')


print("Links -->")
for link in links:
  print(link.get('href'))