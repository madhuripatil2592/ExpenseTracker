from tkinter import *
from tkinter import ttk
import tkinter as tk
from api import ExpenseTrackerDatabase as db
import pandas as pd

class viewexpenseForm():
    def __init__(self):
        self.root=Tk()
        self.root.geometry("500x500")

        self.strmonth=tk.StringVar(self.root)
        self.stryear=tk.StringVar(self.root)

        self.title=Label(self.root,text="View Expense")
        self.lbl1=Label(self.root,text="Search By")
        self.lblmonth=Label(self.root,text="Month")
        self.txtmonth=ttk.Combobox(self.root,textvariable=self.strmonth,values=[i for i in range(1,12)])

        self.lblyear=Label(self.root,text="Year")
        self.txtyear=ttk.Combobox(self.root,textvariable=self.stryear,values=[i for i in range(2020,2025)])

        self.btnsearch=Button(self.root,text="Search",command=self.showExpense)



        self.title.grid(row=0,column=1)
        self.lbl1.grid(row=1,column=1)
        self.lblmonth.grid(row=2,column=0)
        self.txtmonth.grid(row=2,column=1)
        self.lblyear.grid(row=3,column=0)
        self.txtyear.grid(row=3, column=1)
        self.btnsearch.grid(row=5,column=1)


        self.root.mainloop()

    def pushdetail(self,i,j,val,bcolor,fcolor):
        #self.lblstr=tk.StringVar(self.root)
        sticky = {"sticky": "nswe"}
        self.l=Label(self.root,width=10,fg=fcolor,bg=bcolor,text=val)
        self.l.grid(row=i,column=j,pady=1,padx=1,**sticky)

    def showExpense(self):
        print("Show Expense Function")
        month=self.txtmonth.get()
        year=self.txtyear.get()
        print("month=",month)
        print("year=",year)
        record=db.view_expense(month,year)
        df=pd.DataFrame(record)
        print("df columns",df.columns)
        cols=['tid','uid','amount','source','category','paymode','DATE']

        i=10
        for j in range(0,len(cols)):
            self.pushdetail(i,j,cols[j],'blue','black')
        i=i+1

        for r in df.index:
            print(r)
            for j in range(0,len(cols)):
                self.pushdetail(i,j,df.at[r,cols[j]],'yellow','black')
            i=i+1

#v=viewexpenseForm()
