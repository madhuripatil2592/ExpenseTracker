import tkinter as tk
# from tkinter import Tk as ThemedTk
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
import user as userpage

class MyFrame(ThemedTk):



    def __init__(self):
        ThemedTk.__init__(self)
        self.user=""
        self.sum=0
        self.welcomeuser=ttk.Label(self)
        self.welcomeuser.grid(row=8,column=0)
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

        self.login = Menu(menubar, tearoff=0,)
        self.login.add_command(label="Sign In", command=self.loginpage)
        self.login.add_command(label="Sign Up", command=self.addreged)
        self.login.add_command(label="Exit")
        menubar.add_cascade(label="Login", menu=self.login)

        self.transaction = Menu(menubar, tearoff=0)
        self.transaction.add_command(label="Add Income", command=self.addincomed)
        self.transaction.add_command(label="Add Expense", command=self.addexpensed)
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
        self.lblincome = ttk.Label(self)
        sticky = {"sticky": "nswe"}
        self.lblincome.grid(row=6, column=0, columnspan=2, **sticky, pady=10, padx=30)
        self.lblincome.config(relief="solid", width=25, background='red', foreground='black',
                              font=("Times", "15", "bold "))
        self.txttotalincome = ttk.Label(self)
        self.txttotalincome.grid(row=6,column=4)
        self.txttotalincome.config(background='red',foreground='black',font=("Times", "15", "bold "))

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
            log = self.txtuser.get()
            pwd = self.txtpass.get()
            user = db.chk_login(log, pwd)
            if user != 0:
                self.user = user
                self.frame.destroy()

                self.welcomeuser['text']="Welcome",self.user.first
                #print("from user obj fname",userpage.User.uid)
                print("Login Successuful")

                self.loginDone = TRUE
            else:
                self.lblwrong['text'] = "Incorrect Username or Password"

    def homepage(self):
        a = hm.homePage()
        a.root.mainloop()

    def addincomed(self):
        if self.loginDone == TRUE:
            a = ae.addincomeForm()
            a.root.mainloop()

    def addexpensed(self):
        if self.loginDone == TRUE:
            a = exp.addexpenseForm(self.user)
            a.root.mainloop()

    def addreged(self):
        a = reg.addregistrationForm()
        a.root.mainloop

    def viewincomed(self):
        if self.loginDone == TRUE:
            a = vi.viewincomeForm()
            a.root.mainloop

    def viewexpensed(self):
        if self.loginDone == TRUE:
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
        print("total income")
        x = datetime.datetime.now()
        month = x.strftime("%m")
        year = x.strftime("%Y")
        record = db.view_totalincome(month, year)
        for r in record:
            self.sum=self.sum+int(r['amount'])
            print("sum",self.sum)

        #self.lblincome.config(text=self.sum)
        #df = pd.DataFrame(record)
        #print(df.columns)
        #cols = ['tid', 'uid', 'amount', 'source', 'DATE']

    # print("sum=",sum(df['amount']))
    # print(self.strincome.get())
    # self.strincome.set(sum(df['amount']))

    def pushdetails(self):
        self.lblincome = ttk.Label(self.root, text=" TOTAL INCOME :  ")
        sticky = {"sticky": "nswe"}
        self.lblincome.grid(row=6, column=0, columnspan=2, **sticky, pady=10, padx=30)
        self.lblincome.config(relief="solid", width=25, background='red', foreground='black',
                              font=("Times", "15", "bold "))



# main
if __name__ == '__main__':
    MyFrame = MyFrame()
    MyFrame.set_theme("blue")
    MyFrame.mainloop()
    #MyFrame.total_income()