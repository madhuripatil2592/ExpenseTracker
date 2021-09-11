from tkinter import *
from tkinter import ttk
import tkinter as tk
from datetime import date
from api import ExpenseTrackerDatabase as db
import user as U


class addexpenseForm():
    def __init__(self,user):

        self.root=tk.Tk()
        self.user=user

        self.root.geometry("500x500")
        self.username=user.uname
        self.userid=''

        self.strtid=tk.StringVar(self.root)
        self.struid=tk.StringVar(self.root)
        self.stramt=tk.StringVar(self.root)
        self.strsource=tk.StringVar(self.root)
        self.strpaymode=tk.StringVar(self.root)
        self.strcategory=tk.StringVar(self.root)

        self.emptyamt=Label(self.root)
        self.emptysource=Label(self.root)
        self.emptypaymode=Label(self.root)
        self.emptycategory=Label(self.root)


        self.lbltitle=Label(self.root,text="Add Expense")
        self.lblamount=Label(self.root,text="Amount")
        self.lblsource=Label(self.root,text="Source")
        self.lblcategory=Label(self.root,text='Category')
        self.lblpaymode=Label(self.root,text='PayMode')


        self.txtamount=Entry(self.root,textvariable=self.stramt)
        #self.txtcategory=Entry(self.root,textvariable=self.strcategory)
        #self.txtsource=Entry(self.root,textvariable=self.strsource)

        self.txtmode = ttk.Combobox(self.root,textvariable=self.strpaymode,
                                    values=[
                                        "cash",
                                        "card",
                                        "Online"])
        self.txtsource=ttk.Combobox(self.root,textvariable=self.strsource,
                                    values=['Home Expenses',
                                            'Daily Living',
                                            'Childern',
                                            'Medical',
                                            'Entertainment'])

        self.radioimp = Radiobutton(self.root, text='Important', value='important', var=self.strcategory)
        self.radiourgent = Radiobutton(self.root, text='Urgent', value='urgent', var=self.strcategory)
        self.radiounnecessary = Radiobutton(self.root, text='Unnecessary', value='unnecessary', var=self.strcategory)
        #self.txtcategory=ttk.Combobox(self.root,textvariable=self.strcategory,
          #                            values=['important',
           #                                   'urgent',
             #                                 'unnecessary'])


        self.btnsubmit=Button(self.root,text="Submit",command=self.insert_expense1)


        self.lbltitle.grid(row=0,column=0)
        self.lblamount.grid(row=3,column=0)
        self.txtamount.grid(row=3,column=1)
        self.emptyamt.grid(row=3,column=2)
        self.lblsource.grid(row=4,column=0)
        self.txtsource.grid(row=4,column=1)
        self.emptysource.grid(row=4,column=2)
        self.lblcategory.grid(row=5,column=0)
        self.radioimp.grid(row=5,column=1)
        self.radiourgent.grid(row=5,column=2)
        self.radiounnecessary.grid(row=5,column=3)
        self.emptycategory.grid(row=5,column=4)
        self.lblpaymode.grid(row=6,column=0)
        self.txtmode.grid(row=6,column=1)
        self.emptypaymode.grid(row=6,column=2)
        self.btnsubmit.grid(row=7,column=0)

        self.root.mainloop()

    def getusername(self):
        print("Username",U.User.first)

    def insert_expense1(self):
        username=self.username
        amt=self.stramt.get()
        source=self.strsource.get()
        category=self.strcategory.get()
        mode=self.strpaymode.get()

        d=str(date.today())
        #print(tid,uid,amt,source,category,mode,d)
        db.add_expense(username,int(amt),source,category,mode,d)
        print("record inserted",username,amt,source,category,mode)


    def validation(self):
        if self.stramt.get()=='':
            self.e

        self.stramt = tk.StringVar(self.root)
        self.strsource = tk.StringVar(self.root)
        self.strpaymode = tk.StringVar(self.root)
        self.strcategory = tk.StringVar(self.root)

a=addexpenseForm(U.User("111","rani","rani"))

