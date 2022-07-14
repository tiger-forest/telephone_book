import string
letters = tuple(string.ascii_letters)
with open("pnbook.txt", "a", encoding="utf-8"):  # 如果没有这个文件，创建一个
    pass


def new(people, phone_num, comment):  # 定义一个新建信息的函数
    if people in letters:
        print('姓名请勿使用单个字母')
    else:
        with open("pnbook.txt", 'a') as pnbook:
            if comment:
                pnbook.write(f"{people} {phone_num} {comment}///")
            else:
                pnbook.write(f"{people} {phone_num} 无///")


def get_dic(mod='num'):  # 定义一个获取所有联系人信息字典的函数
    with open("pnbook.txt", 'r') as pnbook:
        tp = pnbook.read().split('///')
        tp.pop()
        d = {}
        try:
            for i in tp:
                t = i.split()
                if mod == 'num':
                    d[t[0]] = t[1]
                if mod == 'com':
                    d[t[0]] = t[2]
        except IndexError:
            pass
    return d


def ffind(people):  # 定义一个查找信息的函数
    d = get_dic()
    l = []
    if d:
        for k1 in d.keys():
            if people in k1:
                l.append(k1)
    return l
#    return d.get(people, False)


print('''*欢迎来到电话簿小程序*
请输入内容以查找联系人信息
直接回车以显示全部联系人信息
输入“N”新建一个联系人信息
输入“D”清空存储
输入“Q”退出
不区分大小写
-----------------------------''')
while True:
    tmp = input("请输入：").upper()
    if tmp == 'N':
        p = input("姓名：")
        n = input("电话：")
        c = input("备注：")
        new(p, n, c)
    elif tmp == 'D':
        q = input("你确定要删除全部项吗？此操作不可恢复！（Y/N）").upper()
        if q == 'Y':
            with open("pnbook.txt", "w", encoding="utf-8"):  # 清空
                pass
        else:
            print('--已取消--')
    elif tmp == 'Q':
        break
    elif tmp == '':
        f = ffind(tmp)
        if f:
            for i in f:
                print(f"{i}的电话号为{get_dic()[i]}。  备注：{get_dic('com')[i]}。")
        else:
            print('（空）')
    print('-'*15)
