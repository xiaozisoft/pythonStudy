# code
from bs4 import BeautifulSoup
import requests
import time
import json
import sys
# 头部信息 #需根据自己浏览器的信息进行替换
headers = {
    'Referer': 'http://music.163.com/',
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}


def record_info(filename, info):
    with open(filename,  'a', encoding='utf-8') as openfile:
        json.dump(info, openfile, ensure_ascii=False)
        openfile.write('\n')


def get_artist_songs(filename, artistname):
    with open(filename, 'r', encoding='utf-8') as openfile:
        for line in openfile:
            load_dic = json.loads(line)
            if artistname in load_dic:
                print(load_dic[artistname])
                return load_dic[artistname]


# 获取歌手信息
def get_artist_info(artist_id):
    artist_info = dict()
    play_url = 'https://music.163.com/artist?id=' + str(artist_id)
    # print(play_url)
    s = requests.session()
    s = BeautifulSoup(s.get(play_url, headers=headers).content, 'lxml')
    # print(s)
    songs_info = dict()
    nametext = s.select('h2')
    if len(nametext) != 0:
        # print('歌手：{} 歌手Id：{}'.format(nametext[0].text, nametext[0].attrs['data-rid']))
        main = s.select('ul.f-hide li a')
        for music in main:
            # print(type(music))
            song_id = music['href'][music['href'].find('id=') + len('id='):]
            songs_info.update({music.text: song_id})
            # print('歌曲名称：{},歌曲Id：{}'.format(music.text, song_id))
        artist_info.update({nametext[0].text: {artist_id: songs_info}})
    return artist_info


if __name__ == "__main__":
    print('开始下载歌曲...\n================================================')

    start_time = time.time()  # 开始时间
    storename = "./test.txt"
    for artistid in range(1900, 20000):
        test = get_artist_info(artistid)
        if len(test) != 0:
            # print(test)
            # record_info(storename, test)
            record_info(storename, test)
            #get_artist_songs(storename, 'Andy Kao')
            #get_artist_songs(storename, 'Andy Kao')

    end_time = time.time()  # 结束时间
    print("程序耗时%f秒." % (end_time - start_time))
