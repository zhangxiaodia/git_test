"""
编写一个通讯录程序，实现增删改查功能
1.设计数据结构
一条记录： 姓名，电话， id
一个通讯录：列表，里面元素为记录
2. 函数设计
增加 add_record
查询 query_record
修改 change_record
删除 delete_record
"""

import os

class Address_list:
    def __init__(self):
        self.file = "/Users/admin/git_test/test_data/add_list.txt"

    def open_file(self):
        f = open(self.file)

        for line in f.readlines():
            # print(line)
            info = line.split(",")
            print(info[0])
            print(info[1])
            print(info[2])

    def add_record(self, name, tel, no):
        if no in self.dict:
            print("{}已存在".format(no))
        else:
            dict1 = {no: [name, tel]}
            self.dict.update(dict1)
            print("成功添加{}".format(no))

    def query_record(self, no):
        if no in self.dict:
            print("用户的名称为{}".format(self.dict[no][0]))
            print("用户的联系方式为{}".format(self.dict[no][1]))
        else:
            print("此用户{}不存在，请输入已存在的用户编号，或者添加此用户到通讯录".format(no))

    def change_record(self, no, name, tel):
        if no in self.dict:
            self.dict[no][0] = name
            self.dict[no][1] = tel
            print("此用户{}的信息已更改成功".format(no))
        else:
            print("此用户{}不存在，请输入已存在的用户编号，或者添加此用户到通讯录".format(no))

    def delete_record(self, no):
        if no in self.dict:
            del self.dict[no]
            print("此用户{}删除成功".format(no))
        else:
            print("此用户{}不存在，请输入已存在的用户编号".format(no))

    def save_record(self):

        file_path = "/Users/admin/git_test/test_data/"

        try:
            f = open(file_path+"add_list.txt", "r+", encoding='utf-8')
            f.read()
        except FileNotFoundError:
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            f = open(file_path+"add_list.txt", "w+", encoding='utf-8')

        for i in self.dict:
            f.write(i + "\t" + self.dict[i][0] + "\t" + self.dict[i][1] + '\n')
        f.close()