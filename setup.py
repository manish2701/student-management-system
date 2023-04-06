import mysql.connector

con = mysql.connector.connect(user='root', password='Manish@2701',host='localhost')

cursor = con.cursor()

cursor.execute("create database student;")
cursor.execute("use student;")
cursor.execute("create table students (roll_no int(10), name varchar(20), email varchar(30), gender varchar(20), contact int(11), dob varchar(10), address varchar(50));")