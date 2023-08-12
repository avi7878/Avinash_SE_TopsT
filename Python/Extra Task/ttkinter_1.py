from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("500x500")
root.title("Employee Registration.")
# root.resizable(width="false",height="false")

l_id = Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname = Label(root,text="First Name ")
l_fname.place(x=50,y=100)

l_lname = Label(root,text="Last Name ")
l_lname.place(x=50,y=150)

l_email = Label(root,text="Email ")
l_email.place(x=50,y=200)

l_mobile = Label(root,text="Mobile ")
l_mobile.place(x=50,y=250)

e_id = Entry(root)
e_id.place(x=150,y=50)

e_fname = Entry(root)
e_fname.place(x=150,y=100)

e_lname = Entry(root)
e_lname.place(x=150,y=150)

e_email = Entry(root)
e_email.place(x=150,y=200)

e_mobile = Entry(root)
e_mobile.place(x=150,y=250)

insert = Button(root,text="insert")
insert.place(x=50,y=300)

search = Button(root,text="search")
search.place(x=100,y=300)

update = Button(root,text="update")
update.place(x=155,y=300)

delete = Button(root,text="delete")
delete.place(x=215,y=300)

root.mainloop()