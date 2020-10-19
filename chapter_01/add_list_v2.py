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
        
        f = open(self.file, "r+", encoding='utf-8')
        result = True
        for i in f.readlines():
            info = i.split(",")
            if no == info[0]:
                result = False
                print("此用户{}已存在，请输入不存在的用户信息".format(no))
        if result:
                f.write(no + "," + name + "," + tel + '\n')
                print("此用户{}已添加成功".format(no))

    def query_record(self, no):

        num = 0
        f = open(self.file)
        for i in f.readlines():
            info = i.split(",")
            if no == info[0]:
                num += 1
                print("用户名为{}".format(info[1]))
                print("联系方式为{}".format(info[2]))
        if not num:
            print("此用户{}不存在，请输入已存在的用户编号".format(no))

    def change_record(self, no, name, tel):

        f = open(self.file, "r+", encoding='utf-8')
        lines = f.readlines()
        result = False
        with open(self.file,'w+',encoding="utf-8") as f_new:
            for i in lines:
                info = i.split(",")
                if no == info[0]:
                    result = True
                    f_new.write(no + "," + name + "," + tel + '\n')
                    print("此用户{}已更新成功".format(no))
                else:
                    f_new.write(info[0] + "," + info[1] + "," + info[2] + '\n')
        if not result:
            print("此用户{}未查询到".format(no))


    def delete_record(self, no):

        f = open(self.file, "r+", encoding='utf-8')
        lines = f.readlines()
        with open(self.file, 'w+', encoding="utf-8") as f_new:
            for i in lines:
                info = i.split(",")
                if no == info[0]:
                    print("此用户{}已被删除".format(no))
                else:
                    f_new.write(info[0] + "," + info[1] + "," + info[2] + '\n')


