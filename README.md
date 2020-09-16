# Billing System

Description:- GUI based application and Tkinter module used for GUI applications.Project is built using Python technology, and also used the software Pycharm.Pycharm link https://www.jetbrains.com/pycharm/.This is used to maintain the bills of the customers of their goods like grocery, cosmetics etc.If customer want to get his/her bill somehow lost it,we can give a duplicate copy of it.So, we can provide the copy of the bill.That's good to maintain the good relation between customer-seller.

Sample code:

from tkinter import *
import tkinter.messagebox as tmsg
import random
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def savefile():
    global file
    if Customer_Name.get()=="" or Contact.get()=="" or Bill=="":
        tmsg.showinfo("Error","All field are required")
    else:
        if file == NONE:
            file=asksaveasfilename(initialfile='Untitled',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
            if file=="":
                file=NONE
            else:
                f=open(file,"w")
                f.write(textarea.get(1.0,END))
                f.close()

                root.title(os.path.basename(file)+"Billing")
                print("File saved")
        else:
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()

def exit1():
    ask=tmsg.askyesno('Exit','Are you sure to exit?')
    if ask>0:
        root.destroy()

def total():
    total_cosmetic_price=(
                            (Soap.get() * 40)+
                            (Gell.get()*140)+
                            (Cream.get()*200)+
                            (Face_wash.get()*210)+
                            (Spray.get()*210)+
                            (Comb.get()*50)

    )
    cosmetic_price.set("Rs."+str(total_cosmetic_price))
    c_tax=total_cosmetic_price*0.05
    cosmetic_tax.set("Rs."+str(c_tax))

    total_grocery_price = (
                                  (Rice.get() * 40)+
                                  (Wheat.get() * 200)+
                                  (Sugar.get() * 150)+
                                   (Food_oil.get() * 110)+
                                    (Tea.get() * 120)+
                                     (Daal.get() * 90)
    )
    grocery_price.set("Rs."+str(total_grocery_price))
    g_tax=total_grocery_price*0.05
    grocery_tax.set("Rs."+str(g_tax))

    total_coldrink_price = (
                                   (Limca.get() * 90)+
                                   (Dew.get() * 90)+
                                   (Maaza.get() * 90)+
                                   (Coke.get() * 90)+
                                   (Slice.get() * 90)+
                                   (Thumbsup.get() * 90)
    )
    colddrink_price.set("Rs."+str(total_coldrink_price))
    cd_tax=total_coldrink_price*0.05
    colddrink_tax.set("Rs."+str(cd_tax))

def clear():
    Soap.set(0)
    Gell.set(0)
    Cream.set(0)
    Face_wash.set(0)
    Spray.set(0)
    Comb.set(0)

    Rice.set(0)
    Wheat.set(0)
    Sugar.set(0)
    Food_oil.set(0)
    Tea.set(0)
    Daal.set(0)

    Limca.set(0)
    Dew.set(0)
    Maaza.set(0)
    Coke.set(0)
    Slice.set(0)
    Thumbsup.set(0)

    cosmetic_price.set('')
    grocery_price.set('')
    colddrink_price.set('')
    cosmetic_tax.set('')
    grocery_tax.set('')
    colddrink_tax.set('')

def welcome_bill():
    textarea.delete('1.0',END)
    textarea.insert(END,"\tWelcome to Retail")
    textarea.insert(END, f"\n Bill:{Bill.get()}")
    textarea.insert(END, f"\n Contact:{Contact.get()}")
    textarea.insert(END, f"\n Customer Name:{Customer_Name.get()}")
    textarea.insert(END, f"\n --------------------------------------")
    textarea.insert(END, f"\n Products\t\t Qty\t\tPrice")
    textarea.insert(END, f"\n --------------------------------------")


def bill_area():
    if Customer_Name.get()=="" or Contact.get()=="" or Bill=="":
        tmsg.showinfo("Error","All field are required")
    elif cosmetic_price.get()=='Rs.0.0' and grocery_price.get()=='Rs.0.0' and colddrink_price=='Rs.0.0':
        tmsg.showinfo('Error','No Product Purchased')
    else:
        welcome_bill()
        if Soap.get()!=0:
            textarea.insert(END, f"\n Bath Soap\t\t{Soap.get()}\t\t{Soap.get()*40}")
        if Gell.get()!=0:
            textarea.insert(END, f"\n  Gell\t\t{Gell.get()}\t\t{Gell.get()*140}")
        if Cream.get()!=0:
            textarea.insert(END, f"\n Cream Soap\t\t{Cream.get()}\t\t{Cream.get()*200}")
        if Face_wash.get()!=0:
            textarea.insert(END, f"\n Face Wash\t\t{Face_wash.get()}\t\t{Face_wash.get()*210}")
        if Spray.get()!=0:
            textarea.insert(END, f"\n Spray \t\t{Spray.get()}\t\t{Spray.get()*210}")
        if Comb.get()!=0:
            textarea.insert(END, f"\n Comb \t\t{Comb.get()}\t\t{Comb.get()*50}")

        if Rice.get()!=0:
            textarea.insert(END, f"\n Rice\t\t{Rice.get()}\t\t{Rice.get() * 40}")
        if Wheat.get()!=0:
            textarea.insert(END, f"\n  Wheat\t\t{Wheat.get()}\t\t{Wheat.get() * 200}")
        if Sugar.get()!=0:
            textarea.insert(END, f"\n Sugar\t\t{Sugar.get()}\t\t{Sugar.get() * 150}")
        if Food_oil.get()!=0:
            textarea.insert(END, f"\n Food Oil\t\t{Food_oil.get()}\t\t{Food_oil.get() * 110}")
        if Tea.get()!=0:
            textarea.insert(END, f"\n Tea \t\t{Tea.get()}\t\t{Tea.get() * 120}")
        if Daal.get()!=0:
            textarea.insert(END, f"\n Daal\t\t{Daal.get()}\t\t{Daal.get() * 90}")

        if Limca.get()!=0:
            textarea.insert(END, f"\n Limca\t\t{Limca.get()}\t\t{Limca.get() * 90}")
        if Dew.get()!=0:
            textarea.insert(END, f"\n  Dew\t\t{Dew.get()}\t\t{Dew.get() * 90}")
        if Maaza.get()!=0:
            textarea.insert(END, f"\n Maaza\t\t{Maaza.get()}\t\t{Maaza.get() * 90}")
        if Coke.get()!=0:
            textarea.insert(END, f"\n Coke\t\t{Coke.get()}\t\t{Coke.get() * 90}")
        if Slice.get()!=0:
            textarea.insert(END, f"\n Slice \t\t{Slice.get()}\t\t{Slice.get() * 90}")
        if Thumbsup.get()!=0:
            textarea.insert(END, f"\n Thumsup\t\t{Thumbsup.get()}\t\t{Thumbsup.get() * 90}")

        textarea.insert(END, f"\n --------------------------------------")
        if cosmetic_tax.get()!='0.0':
            textarea.insert(END, f"\n Cosmetic Tax\t\t\t\t{cosmetic_tax.get()}")
        if grocery_tax.get()!='0.0':
            textarea.insert(END, f"\n Grocery Tax\t\t\t\t{grocery_tax.get()}")
        if colddrink_tax.get()!='0.0':
            textarea.insert(END, f"\n Cold Drink Tax\t\t\t\t{colddrink_tax.get()}")
        textarea.insert(END, f"\n --------------------------------------")
        # textarea.insert(END, f"\n --------------------------------------")

def open1():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = NONE
    else:
        root.title(os.path.basename(file) + "Record System")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()


root=Tk()
root.geometry("1370x900")
root.title("Billing System")
bg_color="#074463"
title=Label(root,text="Billing System",font='Georgia 30 bold',bg=bg_color,fg='yellow',relief=GROOVE).pack(fill=X)

F1=Frame(root,bg='crimson',relief=GROOVE)
F1.place(x=2,y=60,width=500,height=100)
lbl1=Label(F1,text='Cosmetics',bg=bg_color,fg='white',font='georgia 8 bold',relief=GROOVE).place(x=2,y=0)

# Variables
Customer_Name=StringVar()
cust_label=Label(F1,text='Customer Name',bg=bg_color,fg='white').place(x=2,y=30)
cust_entry=Entry(F1,textvariable=Customer_Name).place(x=2,y=60)

Contact=StringVar()
cont_label=Label(F1,text='Contact',bg=bg_color,fg='white').place(x=160,y=30)
cont_entry=Entry(F1,textvariable=Contact).place(x=160,y=60)

Bill=StringVar()
bill_label=Label(F1,text='Bill NO',bg=bg_color,fg='white').place(x=310,y=30)
bill_entry=Entry(F1,textvariable=Bill).place(x=310,y=60)
x=random.randint(1000,9999)
Bill.set(str(x))


# Cosmetics
Soap=IntVar()
Gell=IntVar()
Cream=IntVar()
Face_wash=IntVar()
Spray=IntVar()
Comb=IntVar()

F2=Frame(root,bg='crimson',relief=GROOVE)
F2.place(x=2,y=170,width=300,height=300)
lbl2=Label(F2,text='Cosmetics',bg=bg_color,fg='white',font='georgia 8 bold',relief=GROOVE).place(x=0,y=2)

# labels
soap_lbl=Label(F2,text='Soap',font='georgia 8 bold').place(x=2,y=40)

gell_lbl=Label(F2,text='Gell',font='georgia 8 bold').place(x=2,y=70)

cream_lbl=Label(F2,text='Cream',font='georgia 8 bold').place(x=2,y=100)

face_lbl=Label(F2,text='Face Wash',font='georgia 8 bold').place(x=2,y=130)

spray_lbl=Label(F2,text='Spray',font='georgia 8 bold').place(x=2,y=160)

comb_lbl=Label(F2,text='Comb',font='georgia 8 bold').place(x=2,y=190)

# Grocery

Rice=IntVar()
Wheat=IntVar()
Sugar=IntVar()
Food_oil=IntVar()
Tea=IntVar()
Daal=IntVar()

F3=Frame(root,bg='crimson',relief=GROOVE)
F3.place(x=330,y=170,width=300,height=300)
lbl3=Label(F3,text='Grocery',bg=bg_color,fg='white',font='georgia 8 bold',relief=GROOVE).place(x=2,y=0)

# labels
rice_lbl=Label(F3,text='Rice',font='georgia 8 bold').place(x=2,y=40)

wheat_lbl=Label(F3,text='Wheat',font='georgia 8 bold').place(x=2,y=70)

sugar_lbl=Label(F3,text='Sugar',font='georgia 8 bold').place(x=2,y=100)

food_lbl=Label(F3,text='Food oil',font='georgia 8 bold').place(x=2,y=130)

tea_lbl=Label(F3,text='Tea',font='georgia 8 bold').place(x=2,y=160)

daal_lbl=Label(F3,text='Daal',font='georgia 8 bold').place(x=2,y=190)


# Cold Drinks

Limca=IntVar()
Dew=IntVar()
Maaza=IntVar()
Coke=IntVar()
Slice=IntVar()
Thumbsup=IntVar()

F4=Frame(root,bg='crimson',relief=GROOVE)
F4.place(x=660,y=170,width=300,height=300)
lbl4=Label(F4,text='Cold Drinks',bg=bg_color,fg='white',font='georgia 8 bold',relief=GROOVE).place(x=2,y=0)

# labels
limca_lbl=Label(F4,text='Limca',font='georgia 8 bold').place(x=2,y=40)

dew_lbl=Label(F4,text='Dew',font='georgia 8 bold').place(x=2,y=70)

maaza_lbl=Label(F4,text='Maaza',font='georgia 8 bold').place(x=2,y=100)

coke_lbl=Label(F4,text='Coke',font='georgia 8 bold').place(x=2,y=130)

slice_lbl=Label(F4,text='Slice',font='georgia 8 bold').place(x=2,y=160)

thumbs_lbl=Label(F4,text='Thumbsup',font='georgia 8 bold').place(x=2,y=190)

# Cosmetics entry
soap_entry=Entry(F2,textvariable=Soap).place(x=110,y=40)

gell_entry=Entry(F2,textvariable=Gell).place(x=110,y=70)

cream_entry=Entry(F2,textvariable=Cream).place(x=110,y=100)

face_entry=Entry(F2,textvariable=Face_wash).place(x=110,y=130)

spray_entry=Entry(F2,textvariable=Spray).place(x=110,y=160)

comb_entry=Entry(F2,textvariable=Comb).place(x=110,y=190)

# Grocery Entry
rice_entry=Entry(F3,textvariable=Rice).place(x=110,y=40)

wheat_entry=Entry(F3,textvariable=Wheat).place(x=110,y=70)

sugar_entry=Entry(F3,textvariable=Sugar).place(x=110,y=100)

food_entry=Entry(F3,textvariable=Food_oil).place(x=110,y=130)

tea_entry=Entry(F3,textvariable=Tea).place(x=110,y=160)

daal_entry=Entry(F3,textvariable=Daal).place(x=110,y=190)

# Cold drink Entry
limca_entry=Entry(F4,textvariable=Limca).place(x=110,y=40)

dew_entry=Entry(F4,textvariable=Dew).place(x=110,y=70)

maaza_entry=Entry(F4,textvariable=Maaza).place(x=110,y=100)

coke_entry=Entry(F4,textvariable=Coke).place(x=110,y=130)

slice_entry=Entry(F4,textvariable=Slice).place(x=110,y=160)

thumbs_entry=Entry(F4,textvariable=Thumbsup).place(x=110,y=190)

# Bill Menu frame

F5=Frame(root,bg='crimson',relief=GROOVE)
F5.place(x=1,y=480,width=500,height=210)
lbl5=Label(F5,text='Bill Menu',bg=bg_color,fg='white',font='georgia 8 bold',relief=GROOVE).place(x=2,y=0)

# labels
cosmetic_price=StringVar()
grocery_price=StringVar()
colddrink_price=StringVar()
cosmetic_tax=StringVar()
grocery_tax=StringVar()
colddrink_tax=StringVar()

cost_price_lbl=Label(F5,text='Total Cosmetic Price',font='georgia 8 bold').place(x=2,y=30)

grocery_price_lbl=Label(F5,text='Total Grocery Price',font='georgia 8 bold').place(x=2,y=60)

cold_price_lbl=Label(F5,text='Total Cold Drink Price',font='georgia 8 bold').place(x=2,y=90)

cost_tax_lbl=Label(F5,text='Total Cosmetic Tax',font='georgia 8 bold').place(x=2,y=120)

grocery_tax_lbl=Label(F5,text='Total Grocery Tax',font='georgia 8 bold').place(x=2,y=150)

cold_tax_lbl=Label(F5,text='Total Cold drink Tax',font='georgia 8 bold').place(x=2,y=180)

# bill entry
cost_price_entry=Entry(F5,textvariable=cosmetic_price).place(x=190,y=30)

grocery_price_entry=Entry(F5,textvariable=grocery_price).place(x=190,y=60)

cold_price_entry=Entry(F5,textvariable=colddrink_price).place(x=190,y=90)

cost_tax_entry=Entry(F5,textvariable=cosmetic_tax).place(x=190,y=120)

grocery_tax_entry=Entry(F5,textvariable=grocery_tax).place(x=190,y=150)

cold_tax_entry=Entry(F5,textvariable=colddrink_tax).place(x=190,y=180)

# billarea
F6=Frame(root,bg='grey',relief=GROOVE,bd=3)
F6.place(x=1000,y=170,width=340,height=400)
lbl6=Label(F6,text='Bill Area',relief=GROOVE).pack(fill=X)
scroll_y=Scrollbar(F6,orient=VERTICAL)
textarea=Text(F6,yscrollcommand=scroll_y.set)
file=NONE
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack(pady=4)

# Buttons
b1=Button(root,text='Generate',command=bill_area,bg=bg_color,fg='white').place(x=660,y=500)
b2=Button(root,text='Exit',command=exit1,bg=bg_color,fg='white').place(x=660,y=550,width=58)
b3=Button(root,text='Total',bg=bg_color,fg='white',command=total).place(x=800,y=500,width=58)
b4=Button(root,text='Clear',bg=bg_color,fg='white',command=clear).place(x=800,y=550,width=58)
b5=Button(F6,text='Open',bg='red',fg='black',command=open1).place(x=0,y=0)
b6=Button(F6,text='Save',bg='red',fg='black',command=savefile).place(x=53,y=0)
welcome_bill()
root.mainloop()

#to contribute
Email: goyal.tanivji@gmail.com



