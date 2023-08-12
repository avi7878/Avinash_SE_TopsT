import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="")

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS STUDENT_FROM")
mydb.commit()

mydb = pymysql.connect(host="localhost",user="root",password="",database="STUDENT_FROM")
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS STUDENT_DETAILS (id int primary key auto_increment, name varchar(20), roll_no int unique, mobile varchar(20), email varchar(50), city varchar(20) )")
mydb.commit()
