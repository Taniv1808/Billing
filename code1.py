
from tkinter import *
from tkinter import ttk
import pymysql

def add():
    conn=pymysql.connect(host='localhost',user='root',password='Tanivgoyal1808',database='stm')
    my_cursor=conn.cursor()
    my_cursor.execute('insert into Student values(%s,%s,%s,%s,%s,%s)',(Roll_No_var.get(),
                                                                       Name_var.get(),
                                                                       Email_var.get(),
                                                                       Gender_var.get(),
                                                                       Contact_var.get(),
                                                                       DOB_var.get()
                                                                       ))
    conn.commit()
    fetch_data()
    clear()
    conn.close()

def fetch_data():
    conn = pymysql.connect(host='localhost', user='root', password='Tanivgoyal1808', database='stm')
    my_cursor = conn.cursor()
    my_cursor.execute("select * from Student")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        Student_Table.delete(*Student_Table.get_children())
        for row in rows:
            Student_Table.insert('',END,values=row)
        conn.commit()
    conn.close()


def clear():
    Roll_No_var.set("")
    Name_var.set("")
    Email_var.set("")
    Gender_var.set("")
    Contact_var.set("")
    DOB_var.set("")

def get(event):
    cur_row=Student_Table.focus()
    contents=Student_Table.item(cur_row)
    row=contents['values']
    print(row)
    Roll_No_var.set(row[0])
    Name_var.set(row[1])
    Email_var.set(row[2])
    Gender_var.set(row[3])
    Contact_var.set(row[4])
    DOB_var.set(row[5])

def update():
    conn = pymysql.connect(host='localhost', user='root', password='Tanivgoyal1808', database='stm')
    my_cursor = conn.cursor()
    my_cursor.execute('update Student set name=%s,email=%s,gender=%s,contact=%s,dob=%s where roll_no=%s', (
                                                                        Name_var.get(),
                                                                        Email_var.get(),
                                                                        Gender_var.get(),
                                                                        Contact_var.get(),
                                                                        DOB_var.get(),
                                                                        Roll_No_var.get()
                                                                        ))
    conn.commit()
    fetch_data()
    clear()
    conn.close()

def delete():
    conn = pymysql.connect(host='localhost', user='root', password='Tanivgoyal1808', database='stm')
    my_cursor = conn.cursor()
    my_cursor.execute("delete from Student where roll_no=%s",Roll_No_var.get())
    conn.commit()
    conn.close()
    fetch_data()
    clear()

def exit():
    root.destroy()

def search():
    conn = pymysql.connect(host='localhost', user='root', password='Tanivgoyal1808', database='stm')
    my_cursor = conn.cursor()
    my_cursor.execute("select * from Student where "+str(Search_var.get())+"Like %"+str(Search_txt.get())+"%")
    rows = my_cursor.fetchall()
    if len(rows) != 0:
        Student_Table.delete(*Student_Table.get_children())
        for row in rows:
            Student_Table.insert('', END, values=row)
        conn.commit()
    conn.close()

root=Tk()

root.geometry('1365x1365')
root.title('Management')
bg_color="#074463"
title=Label(root,text='Student Management System',font='georgia 33 bold',bg=bg_color,fg='yellow').pack(fill=X)

Roll_No=StringVar()
Name=StringVar()
Email=StringVar()
Gender=StringVar()
Contact=StringVar()
DOB=StringVar()

# Frame
Manage_Frame=Frame(root,bg='crimson',bd=3)
Manage_Frame.place(x=20,y=100,width=450,height=560)

#variables
Roll_No_var=StringVar()
Name_var=StringVar()
Email_var=StringVar()
Gender_var=StringVar()
Contact_var=StringVar()
DOB_var=StringVar()
Search_var=StringVar()
Search_txt=StringVar()

m_title=Label(Manage_Frame,text='Manage Students',font='georgia 22 bold').grid(row=0,columnspan=2,pady=20)

roll_lbl=Label(Manage_Frame,text="Roll_No",bg='crimson',fg='white',font='georgia 16 bold')
roll_lbl.grid(row=1,column=1,pady=10,padx=20)

name_lbl=Label(Manage_Frame,text="Name",bg='crimson',fg='white',font='georgia 16 bold')
name_lbl.grid(row=2,column=1,pady=10)

email_lbl=Label(Manage_Frame,text="Email",bg='crimson',fg='white',font='georgia 16 bold')
email_lbl.grid(row=3,column=1,pady=1)

contact_lbl=Label(Manage_Frame,text="Contact",bg='crimson',fg='white',font='georgia 16 bold')
contact_lbl.grid(row=4,column=1,pady=9)

gender_lbl=Label(Manage_Frame,text="Gender",bg='crimson',fg='white',font='georgia 16 bold')
gender_lbl.grid(row=5,column=1,pady=9)

combo_gender=ttk.Combobox(Manage_Frame,textvariable=Gender_var,font='georgia 5 bold',state='readonly')
combo_gender['values']=('Male','Female','others')
combo_gender.grid(row=5,column=2,padx=10)

dob_lbl=Label(Manage_Frame,text="DOB",bg='crimson',fg='white',font='georgia 16 bold')
dob_lbl.grid(row=6,column=1,pady=9)

# Entry
roll_entry=Entry(Manage_Frame,textvariable=Roll_No_var).grid(row=1,column=2)

name_entry=Entry(Manage_Frame,textvariable=Name_var).grid(row=2,column=2)

email_entry=Entry(Manage_Frame,textvariable=Email_var).grid(row=3,column=2)

contact_entry=Entry(Manage_Frame,textvariable=Contact_var).grid(row=4,column=2)

dob_entry=Entry(Manage_Frame,textvariable=DOB_var).grid(row=6,column=2)

# Buttons

b1=Button(Manage_Frame,text="Add",command=add).place(x=30,y=400,width=89)
b2=Button(Manage_Frame,text="update",command=update).place(x=30,y=450,width=89)
b3=Button(Manage_Frame,text="Delete",command=delete).place(x=150,y=400,width=89)
b4=Button(Manage_Frame,text="Clear",command=clear).place(x=150,y=450,width=89)
b5=Button(Manage_Frame,text="Exit",command=exit).place(x=270,y=430,width=89)

# Frame2
Detail_Frame=Frame(root,bg='crimson',bd=5)
Detail_Frame.place(x=500,y=100,width=800,height=560)

search_lbl=Label(Detail_Frame,text='Search',bg='crimson',font='gerogia 16 bold',fg='white')
search_lbl.grid(row=0,column=0)

combo_search=ttk.Combobox(Detail_Frame,textvariable=Search_var,font='georgia 10 bold',state='readonly',width=10)
combo_search['values']=('Roll_No','Name','Contact')
combo_search.grid(row=0,column=1,padx=10)

txt_search=Entry(Detail_Frame,textvariable=Search_txt,font='georgia 10 bold')
txt_search.grid(row=0,column=2)

search_btn=Button(Detail_Frame,text='Search',command=search)
search_btn.grid(row=0,column=3,padx=10)

show_btn=Button(Detail_Frame,text='Show All',command=fetch_data())
show_btn.grid(row=0,column=4)

# Table Frame
Table_Frame=Frame(Detail_Frame,bd=3,bg='crimson',relief=RIDGE)
Table_Frame.place(x=10,y=70,width=760,height=450)

scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
Student_Table=ttk.Treeview(Table_Frame,columns=('roll_no','name','email','contact','gender','dob'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill='x')
scroll_y.pack(side=RIGHT,fill='y')
scroll_x.config(command=Student_Table.xview)
scroll_y.config(command=Student_Table.yview)
Student_Table.heading("roll_no",text="Roll_No")
Student_Table.heading("name",text="Name")
Student_Table.heading("email",text="Email")
Student_Table.heading("contact",text="Contact")
Student_Table.heading("gender",text="Gender")
Student_Table.heading("dob",text="DOB")
Student_Table['show']='headings'

Student_Table.pack(fill=BOTH,expand='yes')
fetch_data()
Student_Table.bind("<Button-1>",get)

root.mainloop()