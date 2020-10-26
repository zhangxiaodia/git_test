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
from add_list_text import Address_list

while True:

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
    
    if s == "1":
        
        no = input("输入用户的编号:")
        name = input("输入新增的用户名:")
        tel = input("输入用户的联系方式:")
        add_record = Address_list()
                
        add_record(name, tel, no)

    elif s == "2":
        
        no = input("输入要查询的用户编号:")
        #type(Address_list)
        query_record = Address_list()

        query_record.query_record(no)

    elif s == "3":
        
        no = input("输入删除的用户编号:")

        query_record = Address_list()
        query_record.delete_record(no)     
        
    elif s == "4":

        no = input("输入需要修改的用户编号:")
        name = input("输入需要修改的用户名:")
        tel = input("输入需要修改的联系方式:")

        query_record = Address_list()
        query_record.change_record(no, name, tel)

    elif s == "5":

        print("即将退出程序")
        break
        
    else:
        print("请输入正确的选项")