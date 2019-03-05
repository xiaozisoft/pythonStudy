import xlrd


def read_excel(filename, row, column):
    print(filename, row, column)

    wb = xlrd.open_workbook(filename)  # 打开文件

    print(wb.sheet_names())  # 获取所有表格名字

    #sheet1 = wb.sheet_by_index(1)  # 通过索引获取表格

    sheet = wb.sheet_by_name("IRS List")  # 通过名字获取表格

    print(sheet)

    print(sheet.name, sheet.nrows, sheet.ncols)
    rows = sheet.row_values(40)  # 获取行内容
    #cols = sheet.col_values(3)  # 获取列内容

    print(rows)
    print("***")

    print(sheet.cell(1, 0).value)  # 获取表格里的内容，三种方式
    print(sheet.cell_value(1, 0))
    print(sheet.row(4000)[0].value)


if __name__ == "__main__":
    print("start generate code")
    read_excel("test.xlsx", 1, 1)
