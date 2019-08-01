import sqlite3

con = sqlite3.connect("./test.db")         #DB File 생성
cur = con.cursor()
   # DB Table 생성
cur.execute("CREATE TABLE if not exists PhoneBook(Name text, PhoneNum text);")
   #DATA 저장
cur.execute("INSERT INTO PhoneBook VALUES('Sometwo', '010-9999-8989');")
con.commit()       # DB에 저장
cur.execute("SELECT * FROM PhoneBook;")
print (cur.fetchone())
print (cur.fetchmany(2))
print (cur.fetchall())
