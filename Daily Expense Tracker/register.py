from tkinter import *
from tkinter import ttk
import tkinter as tk
import validation as v
from api import ExpenseTrackerDatabase as db

class addregistrationForm():
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry('500x500')
        self.root.config(background="light blue")
        self.flag = 0
        self.email=""
        self.contact=""
        self.strfname=tk.StringVar()
        self.strmname=tk.StringVar()
        self.strlname=tk.StringVar()
        self.strgender=tk.StringVar()
        self.stremail=tk.StringVar()
        self.strcontact=tk.StringVar()
        self.strcity=tk.StringVar()
        self.straddress=tk.StringVar()
        self.strusername=tk.StringVar()
        self.strpassword=tk.StringVar()
        self.struid=tk.StringVar()
        self.lbl1=Label(self.root,text="All fields marked * are complusory")
        self.lblfirst=Label(self.root,text="First Name")
        self.lblmiddle=Label(self.root,text="Middle Name")
        self.lbllast=Label(self.root,text="Last Name")
        self.lblgender=Label(self.root,text="Gender")

        self.lblemail=Label(self.root,text="Email")
        self.lblcontact=Label(self.root,text="Contact")
        self.lblcity=Label(self.root,text="city")
        self.lbladdress=Label(self.root,text="Address")
        self.lblusername=Label(self.root,text="Username")
        self.lblpassword=Label(self.root,text="Password")
        self.lbluid=Label(self.root,text="Uid")

        self.txtfirst=Entry(self.root,textvariable=self.strfname)
        self.txtmiddle=Entry(self.root,textvariable=self.strmname)
        self.txtlast=Entry(self.root,textvariable=self.strlname)
        self.radiomale = Radiobutton(self.root, text='Male',value='male',var=self.strgender)
        self.radiofemale = Radiobutton(self.root, text='Female',value='female',var=self.strgender)
        self.txtemail=Entry(self.root,textvariable=self.stremail)
        self.txtcontact=Entry(self.root,textvariable=self.strcontact)
        self.txtcity=Entry(self.root,textvariable=self.strcity)
        self.txtaddress=Entry(self.root,textvariable=self.straddress)
        self.txtusername=Entry(self.root,textvariable=self.strusername)
        self.txtpassword=Entry(self.root,textvariable=self.strpassword)
        self.txtuid=Entry(self.root,textvariable=self.struid)

        self.btnregister=Button(self.root,text="Register",command=self.validation1)



        self.lblemptyfname=Label(self.root)
        self.lblemptymname=Label(self.root)
        self.lblemptylname=Label(self.root)
        self.lblemptygender =Label(self.root)
        self.lblemptyemail =Label(self.root)
        self.lblemptycontact =Label(self.root)
        self.lblemptycity = Label(self.root)
        self.lblemptyaddress = Label(self.root)
        self.lblemptyusername = Label(self.root)
        self.lblemptypassword = Label(self.root)
        self.lblemptyuid = Label(self.root)

        self.lbl1.grid(row=0,column=0)
        self.lblfirst.grid(row=1,column=0)
        self.txtfirst.grid(row=1,column=1)
        self.lblemptyfname.grid(row=1,column=2)
        self.lblmiddle.grid(row=2,column=0)
        self.txtmiddle.grid(row=2,column=1)
        self.lblemptymname.grid(row=2,column=2)
        self.lbllast.grid(row=3,column=0)
        self.txtlast.grid(row=3,column=1)
        self.lblemptylname.grid(row=3,column=2)
        self.lblgender.grid(row=4,column=0)
        self.radiomale.grid(row=4,column=1)
        self.radiofemale.grid(row=4,column=2)
        self.lblemptygender.grid(row=4,column=3)

        self.lblemail.grid(row=5,column=0)
        self.txtemail.grid(row=5,column=1)
        self.lblemptyemail.grid(row=5,column=2)
        self.lblcontact.grid(row=6,column=0)
        self.txtcontact.grid(row=6,column=1)
        self.lblemptycontact.grid(row=6,column=2)
        self.lblcity.grid(row=7,column=0)
        self.txtcity.grid(row=7,column=1)
        self.lblemptycity.grid(row=7,column=2)
        self.lbladdress.grid(row=8,column=0)
        self.txtaddress.grid(row=8,column=1)
        self.lblemptyaddress.grid(row=8,column=2)
        self.lblusername.grid(row=9,column=0)
        self.txtusername.grid(row=9,column=1)
        self.lblemptyusername.grid(row=9,column=2)
        self.lblpassword.grid(row=10,column=0)
        self.lblemptypassword.grid(row=10,column=2)
        self.txtpassword.grid(row=10,column=1)


        #self.txtuid.grid(row=11,column=1)
        self.btnregister.grid(row=12)

        self.root.mainloop()



    def validation1(self):
        print("Welcome to registration form")
        self.flag=1 #valid
        if self.strfname.get() == '':
            self.lblemptyfname['text'] = "Please Enter First Name"
            self.flag = 0
        else:
            self.lblemptyfname['text'] = ''


        if self.strlname.get() == '':
            self.lblemptylname['text'] = "Please Enter Last Name"
            self.flag=0
        else:
            self.lblemptylname['text'] = ''


        if self.strmname.get() == '':
            self.lblemptymname['text'] = "Please Enter Middle Name"
            self.flag = 0
        else:
            self.lblemptymname['text'] = ''


        if self.strgender.get() == '':
            self.lblemptygender['text'] = 'Please Select Gender'
            self.flag = 0
        else:
            self.lblemptygender['text'] = ''


        if self.strcity.get()=='':
            self.lblemptycity['text']='Please Enter Ciyt'
            self.flag = 0
        else:
            self.lblemptycity['text']=''


        if self.straddress.get()=='':
            self.lblemptyaddress['text']='Please Enter Address'
            self.flag = 0
        else:
            self.lblemptyaddress['text']=''


        if self.strusername.get()=='':
            self.lblemptyusername['text']="Please Enter Username"
            self.flag = 0
        else:
            self.lblemptyusername['text']=''


        if self.strpassword.get()=='':
            self.lblemptypassword['text']='Please Enter Password'
            self.flag = 0
        else:
            self.lblemptypassword['text']=''


        # if self.strcontact.get()=='':
        #     self.lblemptycontact['text']="Please Enter Contact Number"
        #     self.flag = 0
        # else:
        #     self.contact=str(self.strcontact)
        #     res=v.checkcontact(self.contact)
        #     if res == 0:
        #         self.lblemptycontact['text']="Please Enter Valid Contact Number"
        #         self.flag = 0
        #     else:
        #         self.lblemptycontact['text']=''
        #
        # if self.stremail.get()=='':
        #    self.lblemptyemail['text']="Please Enter Email"
        #    self.flag = 0
        # else:
        #    self.email=str(self.stremail)
        #    res=v.checkemail(self.email)
        #    print("res=",res)
        #    if res == 0:
        #        self.lblemptyemail['text']="Please Enter valid Email"
        #        self.flag = 0
        #    else:
        #        self.lblemptyemail['text'] == ''


        if self.flag==1: #all value are valid...
            print("flag insert called")
            self.insert_register()




        #self.insert_register()




    def insert_register(self):
        print("insert function in form")
        fname=self.strfname.get()
        mname=self.strmname.get()
        lname=self.strlname.get()
        gender=self.strgender.get()
        email=self.stremail.get()
        contact=self.strcontact.get()
        city=self.strcity.get()
        address=self.straddress.get()
        username=self.strusername.get()
        password=self.strpassword.get()
        #print('fname',fname)
        db.add_register(fname,mname,lname,gender,email,contact,city,address,username,password)

R=addregistrationForm()