# 从网易云音乐下载歌单歌曲
# 参考了这些网址
# https://blog.csdn.net/Ciiiiiing/article/details/62434438
# https://github.com/kunkun1230/Python-/tree/master/%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90%20%E4%B8%8D%E5%86%8D%E7%8A%B9%E8%B1%AB%20%E8%AF%84%E8%AE%BA%E5%88%86%E6%9E%90
# https://www.zhihu.com/question/36081767

from Crypto.Cipher import AES
from bs4 import BeautifulSoup
import base64
import requests
import urllib.request
import os
import time

path = 'E:/music/'
flag = os.path.exists(path)
if not flag:
    os.mkdir(path)

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


if __name__ == "__main__":
    print('开始下载歌曲...\n================================================')
    start_time = time.time()  # 开始时间
    play_url = 'http://music.163.com/playlist?id=393565693'  # 歌单-民谣还在路上

    s = requests.session()
    s = BeautifulSoup(s.get(play_url, headers=headers).content, 'lxml')
    print(s)
    main = s.select('ul.f-hide li a')
    # for music in main:
    # print(music)
    # song_id = music['href'][music['href'].find('id=') + len('id='):]
    # print('歌曲名称：{},歌曲Id：{}'.format(music.text, song_id))
    # get_mp3(music.text, song_id)

    end_time = time.time()  # 结束时间
    print("程序耗时%f秒." % (end_time - start_time))
