import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import date
from api import ExpenseTrackerDatabase as db
import user as us



class addincomeForm():
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("500x500")
        self.username=''

        self.emptyamount=Label(self.root)
        self.emptysource=Label(self.root)


        self.lbl1=Label(self.root,text="Add Income")
        self.lbluid=Label(self.root,text="Uid")
        self.lblamount=Label(self.root,text="Amount")
        self.lblsource=Label(self.root,text="Source")

        self.uid=tk.StringVar(self.root)
        self.strsource=tk.StringVar(self.root)

        self.vsource=tk.StringVar(self.root)
        self.vamount=tk.StringVar(self.root)
        self.txtuid=Entry(self.root,textvariable=self.uid)
        self.txtamount=Entry(self.root,textvariable=self.vamount)

        self.strsource.set('Other')

        self.radioSalary = Radiobutton(self.root, text='Salary', value='Salary', var=self.strsource)
        self.radioRent = Radiobutton(self.root, text='Rent', value='Rent', var=self.strsource)
        self.radioGift = Radiobutton(self.root, text='Gift', value='Gift', var=self.strsource)
        self.radioOther=Radiobutton(self.root,text='Other',value='Other',var=self.strsource)

        self.btnsubmit=Button(self.root,text="Submit",command=self.insert_income)

        self.lbl1.grid(row=0,column=0)
        self.lbluid.grid(row=2,column=0)
        self.txtuid.grid(row=2,column=1)
        self.lblamount.grid(row=3,column=0)
        self.txtamount.grid(row=3,column=1)
        self.lblsource.grid(row=4,column=0)
        self.radioSalary.grid(row=4,column=1)
        self.radioRent.grid(row=4,column=2)
        self.radioGift.grid(row=4,column=3)
        self.radioOther.grid(row=4,column=4)
        self.btnsubmit.grid(row=5,column=0)
        self.root.mainloop()


    def validation(self):
        pass
    def getusername(self):
        username=us.User.uname
        print("username",username)

    def insert_income(self):
        print("insert_income")
        print("Todays date",date.today())
        uid=self.uid.get()
        source=self.strsource.get()
        amt=self.vamount.get()
        d=str(date.today())

        db.add_income(int(uid),int(amt),source,d)

#a=addincomeForm()

