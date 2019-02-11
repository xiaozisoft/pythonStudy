# coding:utf-8
import requests

url = "http://zmister.com"
data = requests.get(url)
print(data.status_code)

print(data.content)