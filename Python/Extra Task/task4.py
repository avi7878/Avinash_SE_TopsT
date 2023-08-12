from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("500x500")
root.title("Employee Registration.")
root.resizable(width="false",height="false")

l_id = Label(root,text="ID  ")
l_id.place(x=50,y=50)

l_fname = Label(root,text="First Name  ")
l_fname.place(x=50,y=80)

l_lname = Label(root,text="Last Name  ")
l_lname.place(x=50,y=110)

l_email = Label(root,text="Email  ")
l_email.place(x=50,y=140)

l_mobile = Label(root,text="Mobile  ")
l_mobile.place(x=50,y=170)

e_id = Entry(root)
e_id.place(x=150,y=50)

e_fname = Entry(root)
e_fname.place(x=150,y=80)

e_lname = Entry(root)
e_lname.place(x=150,y=110)

e_email = Entry(root)
e_email.place(x=150,y=140)

e_mobile = Entry(root)
e_mobile.place(x=150,y=170)



root.mainloop()
