import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

for story_heading in soup.find_all(class_="indicate-hover css-66vf3i"):
    if story_heading.a:
        print(story_heading.a.text.replace("/n", " ").strip())
    else:
        print(story_heading.contents[0].strip())