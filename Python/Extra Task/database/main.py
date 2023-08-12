import connection
import mysql.connector
import pymysql
from tkinter import *
import tkinter.messagebox as msg

mydb = pymysql.connect(host="localhost",user="root",password="",database="STUDENT_FROM")
mycursor = mydb.cursor()

def create_conn():
    return mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="STUDENT_FROM"
    )

print(create_conn())

def insert_data():
    if e_name.get()=="" or e_rollno.get()=="" or e_mobile.get()=="" or e_email.get()=="" or e_city.get()=="":
        msg.showinfo("Insert Status","All Fields are Mandatory*")
    else:
        conn = create_conn()
        cursor = conn.cursor() # execute the connection
        query = "insert into STUDENT_DETAILS (name,roll_no,mobile,email,city) values (%s,%s,%s,%s,%s)"
        args = (e_name.get(),e_rollno.get(),e_mobile.get(),e_email.get(),e_city.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        msg.showinfo("Insert Status","Data Inserted Successfully.")

    e_name.delete(0,"end")
    e_rollno.delete(0,"end")
    e_mobile.delete(0,"end")
    e_email.delete(0,"end")
    e_city.delete(0,"end")

def search_data():
    e_name.delete(0,"end")
    e_rollno.delete(0,"end")
    e_mobile.delete(0,"end")
    e_email.delete(0,"end")
    e_city.delete(0,"end")

    if e_id.get()=="":
        msg.showinfo("Search Status","ID is Mandatory for Search Operation.")    
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "select * from STUDENT_DETAILS where id=%s"
        args = (e_id.get(),)
        cursor.execute(query,args)
        row = cursor.fetchall()
        if row:
            for i in row:
                e_name.insert(0,i[1])
                e_rollno.insert(0,i[2])
                e_mobile.insert(0,i[3])
                e_email.insert(0,i[4])
                e_city.insert(0,i[5])
        else:
            msg.showinfo("Search Status","ID is not Found!")
            
        conn.close()

def update_data():
    if e_name.get()=="" or e_rollno.get()=="" or e_mobile.get()=="" or e_email.get()=="" or e_city.get()=="":
        msg.showinfo("Update Status","All Fields are Manadatory")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "update STUDENT_DETAILS set name=%s,roll_no=%s,mobile=%s,email=%s,city=%s where id=%s"
        args = (e_name.get(),e_rollno.get(),e_mobile.get(),e_email.get(),e_city.get(), e_id.get())
        
        cursor.execute(query, args)
        conn.commit()
        conn.close()
        msg.showinfo("Update Status","Data is Updated Successfully.")

    e_name.delete(0,"end")
    e_rollno.delete(0,"end")
    e_mobile.delete(0,"end")
    e_email.delete(0,"end")
    e_city.delete(0,"end")

def delete_data():
    if e_id.get()=="":
        msg.showinfo("Delete Status","ID is Mandatory for Delete Operation.")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "delete from STUDENT_DETAILS where id=%s"
        args = (e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        msg.showinfo("Delete Status","ID Delete Successfully.")

    e_id.delete(0,"end")
    e_name.delete(0,"end")
    e_rollno.delete(0,"end")
    e_mobile.delete(0,"end")
    e_email.delete(0,"end")
    e_city.delete(0,"end")

root = Tk()
root.geometry("500x500")
root.title("Employee Registration.")
# root.resizable(width="false",height="false")

l_id = Label(root,text="ID")
l_id.place(x=50,y=50)

l_name = Label(root,text="Name ")
l_name.place(x=50,y=100)

l_rollno = Label(root,text="Roll No ")
l_rollno.place(x=50,y=150)

l_mobile = Label(root,text="Mobile ")
l_mobile.place(x=50,y=200)

l_email = Label(root,text="Email ")
l_email.place(x=50,y=250)

l_city = Label(root,text="City ")
l_city.place(x=50,y=300)

e_id = Entry(root)
e_id.place(x=150,y=50)

e_name = Entry(root)
e_name.place(x=150,y=100)

e_rollno = Entry(root)
e_rollno.place(x=150,y=150)

e_mobile = Entry(root)
e_mobile.place(x=150,y=200)

e_email = Entry(root)
e_email.place(x=150,y=250)

e_city = Entry(root)
e_city.place(x=150,y=300)


insert = Button(root,text="Insert",bg="Black",fg="White",font=("Arial",10),command=insert_data)
insert.place(x=50,y=350)

search = Button(root,text="search",bg="black",fg="white",font=("Arial",10),command=search_data)
search.place(x=100,y=350)

update = Button(root,text="update",bg="black",fg="white",font=("Arial",10),command=update_data)
update.place(x=155,y=350)

delete = Button(root,text="delete",bg="black",fg="white",font=("Arial",10),command=delete_data)
delete.place(x=215,y=350)

root.mainloop()