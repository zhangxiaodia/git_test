"""
main函数
while 循环
选择相应功能 示例

        通讯录
        1. 添加
        2. 查找
        3. 删除
        4. 修改
        5. 退出
"""
from address_list import Address_list

i = True

while i:

    menu = """
    通讯录
    1. 添加
    2. 查找
    3. 删除
    4. 修改
    5. 退出
    """
    print(menu)
    s = input("输入您的操作：")
    list = ("1", "2", "3", "4", "5")
    if s == list[0]:
        
        no = input("输入用户的编号")
        name = input("输入新增的用户名")
        tel = input("输入用户的联系方式")
                
        query_record = Address_list()
        query_record.add_record(name, tel, no)

    elif s == list[1]:
        
        no = input("输入要查询的用户名")

        query_record = Address_list()
        query_record.query_record(no)

    elif s == list[2]:
        
        no = input("输入删除用户名")

        query_record = Address_list()
        query_record.delete_record(no)     
        
    elif s == list[3]:

        no = input("输入需要修改的用户编号")

        query_record = Address_list()
        query_record.change_record(no)

    elif s == list[4]:

        print("即将退出程序")
        i = False
        
    else:
        print("请输入正确的选项")