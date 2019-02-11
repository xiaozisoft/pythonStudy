from bs4 import BeautifulSoup
import requests
import time
import os

# 头部信息 #需根据自己浏览器的信息进行替换
headers = {
    'Referer': 'http://music.163.com/',
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}


# 获取歌手信息
def get_artist_info(artist_id):
    artist_info = dict()
    play_url = 'https://music.163.com/artist?id=' + str(artist_id)
    print(play_url)
    s = requests.session()
    s = BeautifulSoup(s.get(play_url, headers=headers).content, 'lxml')
    # print(s)
    songs_info = dict()
    nametext = s.select('h2')
    if len(nametext) != 0:
        print('歌手：{} 歌手Id：{}'.format(nametext[0].text, nametext[0].attrs['data-rid']))
        main = s.select('ul.f-hide li a')
        for music in main:
            # print(type(music))
            song_id = music['href'][music['href'].find('id=') + len('id='):]
            songs_info.update({music.text: song_id})
            # print('歌曲名称：{},歌曲Id：{}'.format(music.text, song_id))
        artist_info.update({artist_id: {nametext[0].text: songs_info}})
    return songs_info


if __name__ == "__main__":
    print('开始下载歌曲...\n================================================')

    start_time = time.time()  # 开始时间

    for artist_id in range(2000, 2001):
        test = get_artist_info(artist_id)
        if len(test) != 0:
            print(test)

    end_time = time.time()  # 结束时间
    print("程序耗时%f秒." % (end_time - start_time))
