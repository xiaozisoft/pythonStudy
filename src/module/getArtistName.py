# code
from Crypto.Cipher import AES
from bs4 import BeautifulSoup
import base64
import requests
import urllib.request
import time
import json
import os

# 头部信息 #需根据自己浏览器的信息进行替换
headers = {
    'Referer': 'http://music.163.com/',
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}


# 获取参数
def get_params(text):
    first_key = "0CoJUm6Qyw8W8jud"
    second_key = "FFFFFFFFFFFFFFFF"
    h_encText = AES_encrypt(text, first_key)
    h_encText = AES_encrypt(h_encText, second_key)
    return h_encText


# 获取 encSecKey
def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey


# 加密过程
def AES_encrypt(text, key):
    iv = "0102030405060708"
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text)
    encrypt_text = str(encrypt_text, encoding="utf-8")  # 注意一定要加上这一句，没有这一句则出现错误
    return encrypt_text


# 下载歌曲
def get_mp3(name, song_id):
    url = "http://music.163.com/weapi/song/enhance/player/url?csrf_token="  # 网易歌曲前缀

    first_param = '{ids:"[%s]", br:"128000", csrf_token:""}' % song_id
    data = {
        "params": get_params(first_param).encode('utf-8'),
        "encSecKey": get_encSecKey()
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        result = response.json()

        if result['code'] != 200:
            print('!!! 歌曲[%s]下载失败...' % name)
            return

        mp3_url = result['data'][0]['url']
        urllib.request.urlretrieve(mp3_url, os.path.join('E:/music/', name + '.mp3'))
        print('歌曲[%s]下载完成...' % name)
    except:
        print('!!!歌曲[%s]下载出现异常...' % name)


#纪录歌曲信息到文件
def record_info(filename, info):
    with open(filename,  'a', encoding='utf-8') as openfile:
        json.dump(info, openfile, ensure_ascii=False)
        openfile.write('\n')


#从文件获取歌手歌曲信息
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
    '''
    for artistid in range(1900, 20000):
        test = get_artist_info(artistid)
        if len(test) != 0:
            # print(test)
            # record_info(storename, test)
            record_info(storename, test)
    '''
    songsdic = get_artist_songs(storename, '林俊杰')
    for songs in songsdic:
        for song in songsdic[songs]:
            print(song)
            print(songsdic[songs][song])
            get_mp3(song, int(songsdic[songs][song]))
    end_time = time.time()  # 结束时间
    print("程序耗时%f秒." % (end_time - start_time))
