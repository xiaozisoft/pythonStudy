
from Crypto.Cipher import AES
from bs4 import BeautifulSoup
import base64
import requests
import urllib.request
import os
import time

# 头部信息 #需根据自己浏览器的信息进行替换
headers = {
    'Referer': 'http://music.163.com/',
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

if __name__ == "__main__":
    print('开始下载歌曲...\n================================================')
    start_time = time.time()  # 开始时间

    for artist_id in range(2000, 10000):
        play_url = 'https://music.163.com/artist?id=' + str(artist_id)  # 歌单-民谣还在路上
        print(play_url)
        s = requests.session()
        s = s.get(play_url, headers=headers)
        s = BeautifulSoup(s.content,  'lxml')
        # print(s)
        nametext = s.select('h2')
        if len(nametext) != 0:
            print('歌手：{} 歌手Id：{}'.format(nametext[0].text, nametext[0].attrs['data-rid']))
        else:
            continue

        main = s.select('ul.f-hide li a')
        for music in main:
            # print(type(music))
            song_id = music['href'][music['href'].find('id=') + len('id='):]
            print('歌曲名称：{},歌曲Id：{}'.format(music.text, song_id))
            # get_mp3(music.text, song_id)



    end_time = time.time()  # 结束时间
    print("程序耗时%f秒." % (end_time - start_time))
