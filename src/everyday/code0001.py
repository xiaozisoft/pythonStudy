#生成激活码或者优惠券码
import random
import string


def genactivecode(activenum):
    listcode = string.ascii_letters + string.digits
    activeset = random.choices(listcode, activenum)
    print(listcode)
    print(activeset)


if __name__ == '__main__':
    a = genactivecode(200)
    print(a)

