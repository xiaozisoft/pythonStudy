import requests

# 获取外网IP
def get_out_ip():
    url = r'http://2019.ip138.com/ic.asp'
    r = requests.get(url)
    txt = r.text
    ip = txt[txt.find("[") + 1: txt.find("]")]
    print('ip:' + ip)
    return ip


print(get_out_ip())

