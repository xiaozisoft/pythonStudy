# coding:utf-8
import requests
from bs4 import BeautifulSoup

url = "http://root@10.77.52.156/miner_stats.cgi"

wbdata = requests.get(url).text
print('wbdata:', wbdata)
soup = BeautifulSoup(wbdata, "lxml")
print('soup :', soup.prettify())

news_titles = soup.select("div.db > ul.list")
print('*******')
print(type(news_titles))
print(news_titles)
for n in news_titles:
    print(n)