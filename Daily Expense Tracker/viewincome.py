from tkinter import *
from tkinter import ttk
import tkinter as tk
import pandas as pd
from api import ExpenseTrackerDatabase as db

class viewincomeForm():
    def __init__(self):
        self.root=Tk()
        self.root.geometry("500x500")
        self.strincome=tk.StringVar(self.root)
        self.strmonth=tk.StringVar(self.root)
        self.stryear=tk.StringVar(self.root)

        self.lbltitle=Label(self.root,text="View Income")
        self.lblsearch=Label(self.root,text="Search By")
        self.lblmonth=Label(self.root,text="Month")
        self.lblyear=Label(self.root,text='Year')
        self.txtmonth = ttk.Combobox(self.root, textvariable=self.strmonth,values=[i for i in range(1,13) ])
                                      #values=['Jan', 'Feb','March','April','May'])
        self.txtyear= ttk.Combobox(self.root,textvariable=self.stryear,values=[i for i in range(2020,2025) ])



        self.btnsearch=Button(self.root,text="Search",command=self.showincome)

        self.lbltitle.grid(row=0)
        self.lblsearch.grid(row=1,column=0)
        self.lblmonth.grid(row=2,column=0)
        self.txtmonth.grid(row=2,column=1)
        self.lblyear.grid(row=3,column=0)
        self.txtyear.grid(row=3,column=1)
        self.btnsearch.grid(row=4,column=0)
        self.lblincome = ttk.Label(self.root, text=" TOTAL INCOME :  ")
        sticky = {"sticky": "nswe"}
        self.lblincome.grid(row=6, column=0, columnspan=2, **sticky,pady=10,padx=30)
        self.lblincome.config(relief="solid", width= 25,background='red',foreground='black',font=("Times", "15", "bold "))
        self.txtincome = ttk.Label(self.root, text=" TOTAL INCOME :  ",textvariable=self.strincome)

        self.txtincome.grid(row=6, column=2, columnspan=2, **sticky,pady=10,padx=10)
        self.txtincome.config(relief="solid", width= 25,background='yellow',foreground='black',font=("Times", "15", "bold "))
        self.root.mainloop()
    def push_detail(self,i,j,val,bcolor,fcolor):
        sticky = {"sticky": "nswe"}
        self.e = Entry(self.root, width=10, fg=fcolor,bg=bcolor)
        self.e.grid(row=i, column=j,pady=1,padx=1,**sticky)
        self.e.insert(END, val)

    def showincome(self):
        month=self.txtmonth.get()
        year=self.txtyear.get()
        record=db.view_income(month,year)
        df=pd.DataFrame(record)
        print(df.columns)
        cols=['tid','uid','amount', 'source', 'DATE']

        self.strincome.set(sum(df['amount']))
        i=10
        for j in range(0,len(cols)):
                self.push_detail(i,j, cols[j],'blue','black')
        i=i+1
        for r in df.index:
            print(r)
            for j in range(0,len(cols)):
                self.push_detail(i,j, df.at[r,cols[j]],'yellow','black')
            i=i+1
#v=viewincomeForm()
