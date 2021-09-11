from tkinter import *
import tkinter as tk
from api import ExpenseTrackerDatabase as db
import register as reg
import user as User

class LoginPage():
    def __init__(self):
        self.root=Tk()
        self.root.geometry("500x500")

        self.lbl1=Label(self.root,text="Login")
        self.lbluser=Label(self.root,text="User ID")
        self.lblpass=Label(self.root,text="Password")
        self.txtuser=Entry(self.root)
        self.txtpass=Entry(self.root)
        self.btnlogin=Button(self.root,text="Login",command=self.validation)
        self.btnsignup=Button(self.root,text="Sign Up",command=self.signup)
        self.lbl2=Label(self.root,text="Not a member yet....!!")
        self.loginDone=False

        self.emptyusername=Label(self.root)
        self.emptypassword=Label(self.root)
        self.lblwrong=Label(self.root)



        self.lbl1.grid(row=0)
        self.lbluser.grid(row=1,column=0)
        self.txtuser.grid(row=1,column=1)
        self.emptyusername.grid(row=1,column=2)
        self.lblpass.grid(row=2,column=0)
        self.txtpass.grid(row=2,column=1)
        self.emptypassword.grid(row=2,column=2)
        self.btnlogin.grid(row=3)
        self.lbl2.grid(row=4)
        self.btnsignup.grid(row=5,column=1)
        self.lblwrong.grid(row=6,column=1)

        self.root.mainloop()
    def validation(self):
        if self.txtuser.get()=='':
            self.emptyusername['text']='Please Enter Username'
        elif self.txtpass.get()=='':
            self.emptypassword['text']='Please Enter Password'
        else:
            self.chklogin()

    def signup(self):
        a = reg.addregistrationForm()
        self.root.mainloop()


    def chklogin(self):
        print("check login")
        log=self.txtuser.get()
        pwd=self.txtpass.get()
        user=db.chk_login(log,pwd)
        print("user",user)
        #print("home page value of data=",data)
        if(user is User):
            #close current window
            self.loginDone=True
            #findd


        else:
            self.lblwrong['text']="Incorrect Username or Password"
#l=LoginPage()

