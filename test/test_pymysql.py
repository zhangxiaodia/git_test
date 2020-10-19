import pymysql, configparser

config = configparser.ConfigParser()

config.read('/Users/admin/git_test/config/config.ini')

sql_host = config.get('mysql', 'host')
sql_user = config.get('mysql', 'user')
sql_port = config.get('mysql', 'port')
sql_pwd = config.get('mysql', 'password')

del_table_sql = 'drop table if exists phonebook'
create_table_sql = """create table phonebook(
no char(20) not null,
name char(20),
tel char(20) 
)"""
conn = pymysql.connect(host=sql_host, user=sql_user, password=sql_pwd, port=int(sql_port), database='qlove_core_user', charset='utf8')
cursor = conn.cursor()

try:
    result_delete = cursor.execute(del_table_sql)
    result_create = cursor.execute(create_table_sql)
    conn.commit()
except:
    db.rollback()
cursor.close()