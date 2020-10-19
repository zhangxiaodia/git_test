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


class Address_list:
    def __init__(self):
        self.name = "test_name"
        self.tel = "15671559342"
        self.no = 1

    def add_record(self, name, tel, no):

        self.name = name
        self.tel = tel
        self.no = no

    def query_record(self, no):
        if self.no == no:
            print(self.name)
            print(self.tel)

    def change_record(self, no):
        if self.no == no:
            self.name = "name_change"
            self.tel = "tel_change"

    def delete_record(self, no):
        if self.no == no:
            self.name = "name_change"
            self.tel = "tel_change"
