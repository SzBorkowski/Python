import requests
from bs4 import BeautifulSoup

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
soup = BeautifulSoup(r.text)

htmltext = soup.select("ContentHeaderDek-bIqFFZ fYeNbg")

for elem in htmltext[7:]:
  print(elem.text)