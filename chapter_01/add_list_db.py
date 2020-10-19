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

import pymysql
import configparser

config = configparser.ConfigParser()

config.read('/Users/admin/git_test/config/config.ini')

sql_host = config.get('mysql', 'host')
sql_user = config.get('mysql', 'user')
sql_port = config.get('mysql', 'port')
sql_pwd = config.get('mysql', 'password')

conn = pymysql.connect(host=sql_host, user=sql_user, password=sql_pwd, port=int(sql_port),
                           database='qlove_core_user', charset='utf8')


def add_record(name, tel, no):
    

    add_table_sql = 'insert into phonebook(no,name,tel) values ({},{},{})'.format(no, name, tel)
    
    cursor = conn.cursor()

    try:
        cursor.execute(add_table_sql)
        conn.commit()
    except:
        conn.rollback()
    cursor.close()


def query_record(no):

    query_table_sql = 'select * from phonebook where no = {}'.format(no)

    cursor = conn.cursor()

    try:
        cursor.execute(query_table_sql)
        results = cursor.fetchall()
        for row in results:
            name = row[1]
            tel = row[2]
            print("用户名为{}".format(name))
            print("联系方式为{}".format(tel))
        conn.commit()
    except:
        conn.rollback()
    cursor.close()


def change_record(no, name, tel):

    update_table_sql = 'update phonebook set name = {},tel ={} where no = {}'.format(name, tel, no)

    cursor = conn.cursor()

    try:
        cursor.execute(update_table_sql)
        conn.commit()
    except:
        conn.rollback()
    cursor.close()


def delete_record(no):
    del_table_sql = 'delete from phonebook where no = {}'.format(no)

    cursor = conn.cursor()

    try:
        cursor.execute(del_table_sql)
        conn.commit()
    except:
        conn.rollback()
    cursor.close()
