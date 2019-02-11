#_*_coding:utf8 _*_
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

if __name__ == "__main__":
    browser_driver = webdriver.Chrome()

    browser_driver.get("https://studygolang.com/pkgdoc")
    links = []
    titles = []
    browser_driver.switch_to.frame(0)
    for link in browser_driver.find_elements_by_tag_name('a'):
        links.append(link.get_attribute('href'))
        titles.append(link.text)

    file_path = 'E:\est\go_artical{}.htm'
    i = 0
    for res in links:
        result = requests.get(res)
        result.raise_for_status()
        for chunk in result.iter_content(100000):
            playFile = open(file_path.format(i),'wb')
            playFile.write(chunk)
            i = i + 1
            playFile.close()

    browser_driver.quit()
