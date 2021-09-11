import tkinter as tk

def des():
    frame.destroy()

root=tk.Tk()
frame=tk.Frame(root)
#frame.geometry("500x500")
lbluser=tk.Label(frame,text="UserName")
clickme=tk.Button(frame,text="ClickMe",command=des)

frame

lbluser.grid(row=1)
clickme.grid(row=2)

#--------------------------------------------------
import tkinter as tk
# from tkinter import Tk as ThemedTk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd
from tkinter import ttk
from ttkthemes import ThemedTk, THEMES
from tkinter import *
import addincome as ae
import addexpense as exp
import register as reg
import viewincome as vi
import viewexpense as ve
import home as hm
import login as lp
import reports as repo
import datetime
from api import ExpenseTrackerDatabase as db


class MyFrame(ThemedTk):
    def __init__(self):
        ThemedTk.__init__(self)

        self.total_income()
        self.geometry("700x500")
        self.strincome = tk.StringVar(self)
        self.label = ttk.Label(self, text=" WELCOME TO BUDGET ")
        sticky = {"sticky": "nswe"}
        self.label.grid(row=1, column=2, columnspan=2, **sticky, pady=10, padx=30)
        self.label.config(relief="solid", width=50, background='yellow', foreground='purple',
                          font=("Times", "33", "bold italic"))

        menubar = Menu()
        self.config(menu=menubar)
        homemenu = Menu(menubar, tearoff=0)
        # homemenu.add_command(label="Home",command=self.homepage)
        menubar.add_cascade(label="Home", command=self.homepage)
        # menubar.add_cascade(label="Home",command=self.homepage)

        self.transaction = Menu(menubar, tearoff=0)
        self.transaction.add_command(label="Sign In", command=self.loginpage)
        self.transaction.add_command(label="Sign Up", command=self.addreged)
        self.transaction.add_command(label="Exit")
        menubar.add_cascade(label="Login", menu=self.transaction)

        self.transaction = Menu(menubar, tearoff=0)
        self.transaction.add_command(label="Add Income", command=self.addincomed, state=DISABLED)
        self.transaction.add_command(label="Add Expense", command=self.addexpensed, state=DISABLED)
        self.transaction.add_command(label="Close")
        menubar.add_cascade(label="Transaction", menu=self.transaction)

        viewmenu = Menu(menubar, tearoff=0)
        viewmenu.add_command(label="View Income", command=self.viewincomed)
        viewmenu.add_command(label="View Expenses", command=self.viewexpensed)
        menubar.add_cascade(label="View", menu=viewmenu)

        reportmenu = Menu(menubar, tearoff=0)
        reportmenu.add_command(label="UserWiseReport", command=self.userwisereport)
        reportmenu.add_command(label="CategoryWise Report", command=self.categoryreport)
        menubar.add_cascade(label="Reports", menu=reportmenu)

        # home = hm.HomePage()
        self.lblincome = ttk.Label(self, text=" TOTAL INCOME :  ")
        sticky = {"sticky": "nswe"}
        self.lblincome.grid(row=6, column=0, columnspan=2, **sticky, pady=10, padx=30)
        self.lblincome.config(relief="solid", width=25, background='red', foreground='black',
                              font=("Times", "15", "bold "))
        self.txtincome = ttk.Label(self, text=" TOTAL INCOME :  ", textvariable=self.strincome)

        def des():
            self.frame.destroy()

        # root = tk.Tk(self)
        self.frame = tk.Frame(self)
        self.frame.grid(row=10, column=0)
        # frame.geometry("500x500")
        #lbluser = tk.Label(self.frame, text="UserName")
        #clickme = tk.Button(self.frame, text="ClickMe", command=des)

        #lbluser.grid(row=1)
        #clickme.grid(row=2)

        self.lbl1 = tk.Label(self.frame, text="Login")
        self.lbluser = tk.Label(self.frame, text="User ID")
        self.lblpass = tk.Label(self.frame, text="Password")
        self.txtuser = tk.Entry(self.frame)
        self.txtpass = tk.Entry(self.frame)
        self.btnlogin = tk.Button(self.frame, text="Login", command=self.validation)
        self.btnsignup = tk.Button(self.frame, text="Sign Up", command=self.signup)
        self.lbl2 = tk.Label(self.frame, text="Not a member yet....!!")
        self.loginDone = False

        self.emptyusername = tk.Label(self.frame)
        self.emptypassword = tk.Label(self.frame)
        self.lblwrong = tk.Label(self.frame)

        self.lbl1.grid(row=0)
        self.lbluser.grid(row=1, column=0)
        self.txtuser.grid(row=1, column=1)
        self.emptyusername.grid(row=1, column=2)
        self.lblpass.grid(row=2, column=0)
        self.txtpass.grid(row=2, column=1)
        self.emptypassword.grid(row=2, column=2)
        self.btnlogin.grid(row=3)
        self.lbl2.grid(row=4)
        self.btnsignup.grid(row=5, column=1)
        self.lblwrong.grid(row=6, column=1)

        def validation(self):
            if self.txtuser.get() == '':
                self.emptyusername['text'] = 'Please Enter Username'
            elif self.txtpass.get() == '':
                self.emptypassword['text'] = 'Please Enter Password'
            else:
                self.chklogin()

        def signup(self):
            a = reg.addregistrationForm()
            self.root.mainloop()

        def chklogin(self):
            print("check login")
            log = self.txtuser.get()
            pwd = self.txtpass.get()
            user = db.chk_login(log, pwd)
            print("user", user)
            # print("home page value of data=",data)
            if (user is User):
                # close current window
                self.loginDone = True
                # findd


            else:
                self.lblwrong['text'] = "Incorrect Username or Password"

    def homepage(self):
        a = hm.homePage()
        a.root.mainloop()

    def addincomed(self):
        a = ae.addincomeForm()
        a.root.mainloop()

    def addexpensed(self):
        a = exp.addexpenseForm()
        a.root.mainloop()

    def addreged(self):
        a = reg.addregistrationForm()
        a.root.mainloop

    def viewincomed(self):
        a = vi.viewincomeForm()
        a.root.mainloop

    def viewexpensed(self):
        a = ve.viewexpenseForm()
        a.root.mainloop

    def loginpage(self):
        a = lp.LoginPage()
        a.root.mainloop

    def userwisereport(self):
        a = repo.showreport.userwisegraph()
        a.root.mainloop

    def categoryreport(self):
        a = repo.categorywisegraph()
        a.root.mainloop

    def total_income(self):
        x = datetime.datetime.now()
        month = x.strftime("%m")
        year = x.strftime("%Y")
        record = db.view_totalincome(month, year)
        df = pd.DataFrame(record)
        print(df.columns)
        cols = ['tid', 'uid', 'amount', 'source', 'DATE']

    # print("sum=",sum(df['amount']))
    # print(self.strincome.get())
    # self.strincome.set(sum(df['amount']))

    def pushdetails(self):
        self.lblincome = ttk.Label(self.root, text=" TOTAL INCOME :  ")
        sticky = {"sticky": "nswe"}
        self.lblincome.grid(row=6, column=0, columnspan=2, **sticky, pady=10, padx=30)
        self.lblincome.config(relief="solid", width=25, background='red', foreground='black',
                              font=("Times", "15", "bold "))
        self.txtincome = ttk.Label(self.root, text=" TOTAL INCOME :  ", textvariable=self.strincome)


# main
if __name__ == '__main__':
    MyFrame = MyFrame()
    MyFrame.set_theme("blue")
    MyFrame.mainloop()








root.mainloop()

