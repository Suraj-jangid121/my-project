# import sqlite3

# conn=sqlite3.connect("db1.db")
# sql="""
# Create table emp(
# id integer primary key autoincrement,
# name varchar(50),
# mob varchar(50),
# city varchar(50)
# )"""

# conn.execute(sql)
# conn.close()
# import sqlite3

# conn=sqlite3.connect("db1.db")
# sql="""
# insert into emp(name,mob,city) values('vansh','1234567890','delhi')"""

# conn.execute(sql)
# conn.commit()
# conn.close()
# import sqlite3
# conn=sqlite3.connect("db1.db")
# sql="""select * from emp"""
# res=conn.execute(sql)
# for row in res:
#     print(row)
# import sqlite3
# conn=sqlite3.connect("db1.db")

# sql="""update emp set city='noida' where id=1"""    
# conn.execute(sql)
# conn.commit()
# conn.close()
import sqlite3
conn=sqlite3.connect("db1.db")  

sql="""delete from emp where id=1"""
conn.execute(sql)
conn.commit()
conn.close()