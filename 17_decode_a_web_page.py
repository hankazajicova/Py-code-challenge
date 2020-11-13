import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="html.parser")

nyt_titles = []
for element in soup.select('.e1voiwgp0'):
    nyt_titles.append(element.text)


print(nyt_titles)
