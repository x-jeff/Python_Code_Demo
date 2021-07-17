import sqlite3 as lite
import pandas

# 1.使用python链接数据库
# 方法一
# con = lite.connect('test.sqlite')
# cur = con.cursor()
# cur.execute('SELECT SQLITE_VERSION()')
# data = cur.fetchone()
# print(data)
# con.close()
# 方法二
# with lite.connect('test.sqlite') as con:
#   cur = con.cursor()
#   cur.execute('SELECT SQLITE_VERSION()')
#   data = cur.fetchone()
#   print(data)

# 2.透过SQLite做数据新增、查询
with lite.connect('test.sqlite') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS PhoneAddress")
    cur.execute(
        "CREATE TABLE PhoneAddress(phone CHAR(10) PRIMARY KEY, address TEXT, name TEXT unique, age INT NOT NULL)")
    cur.execute("INSERT INTO PhoneAddress VALUES('0912173381','United State','Jhon Doe',53)")
    cur.execute("INSERT INTO PhoneAddress VALUES('0928375018','Tokyo Japan','MuMu Cat',6)")
    cur.execute("INSERT INTO PhoneAddress VALUES('0957209108','China','Zhang San',29)")
    cur.execute("SELECT phone,address FROM PhoneAddress")
    data = cur.fetchall()
    for rec in data:
        print(rec[0], rec[1])

# 3.使用pandas存储数据
# 建立DataFrame
employee = [{'name': 'Mary', 'age': 23, 'gender': 'F'}, {'name': 'John', 'age': 33, 'gender': 'M'}]
df = pandas.DataFrame(employee)
# 使用pandas存储数据
with lite.connect('test.sqlite') as db:
    df.to_sql(name='employee', index=False, con=db, if_exists='replace')
