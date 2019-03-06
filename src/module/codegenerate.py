# -*- coding: UTF-8 -*-

import xlrd


def formatoutput(str):
    s = str.split(' ')
    t = '{0: <7} {1: <30} {2}'.format(s[0], s[1], s[2])
    return t


def read_excel(readfile, writefile):
    fb = open(writefile, "w")
    wb = xlrd.open_workbook(readfile)  # 打开文件
    print(wb.sheet_names())  # 获取所有表格名字

    sheet = wb.sheet_by_name("IRS List")  # 通过名字获取表格
    for row in [sheet.row_values(index) for index in range(1, sheet.nrows)]:
        if len(row[1]):
            strtmp = "#define " + row[2] + "_REG" + " " + row[1]
            strtmp = formatoutput(strtmp)
            print(strtmp)
            fb.write('\n')
            fb.write(strtmp + '\n')
        if row[3] != "reserved":
            a = row[4]
            if len(a) > 2:
                s = a.split(':')
                offset = s[1]
                masklen = int(s[0]) - int(s[1]) + 1
            else:
                masklen = 1
                offset = row[4]

            # print("#define          ", row[3], "_OFFSET", "       ", offset)
            strtmp = "#define " + row[3] + "_OFFSET" + " " + offset
            strtmp = formatoutput(strtmp)
            print(strtmp)
            fb.write(strtmp + '\n')
            # print("#define          ", row[3], "_MASK", "       ", masklen)
            strtmp = "#define " + row[3] + "_MASK" + " " + str(masklen)
            strtmp = formatoutput(strtmp)
            print(strtmp)
            fb.write(strtmp + '\n')
    fb.close()

if __name__ == "__main__":
    read_excel("test.xlsx", "bm18m3l.h")
