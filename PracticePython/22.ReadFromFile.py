import requests
from bs4 import BeautifulSoup

url = 'https://www.practicepython.org/assets/nameslist.txt'
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

with open(r, 'r') as f:
    all_text = f.read()
print(all_text)