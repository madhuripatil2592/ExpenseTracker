import tkinter as tk
#from tkinter import Tk as ThemedTk
from tkinter import ttk
from ttkthemes import ThemedTk, THEMES
from tkinter import *

import register as reg
import home as hm



class MyFrame(ThemedTk):
    def __init__(self):
        ThemedTk.__init__(self)
        self.geometry("700x500")
        self.label = ttk.Label(self, text=" WELCOME TO BUDGET ")
        sticky = {"sticky": "nswe"}
        self.label.grid(row=1, column=2, columnspan=2, **sticky,pady=10,padx=30)
        self.label.config(relief="solid", width= 50,background='yellow',foreground='purple',font=("Times", "33", "bold italic"))

        menubar = Menu()
        self.config(menu=menubar)
        homemenu = Menu(menubar, tearoff=0)
        #homemenu.add_command(label="Home",command=self.homepage)
        menubar.add_cascade(label="Home",command=self.homepage)
        #menubar.add_cascade(label="Home",command=self.homepage)

        transaction=Menu(menubar,tearoff=0)
        transaction.add_command(label="Add Income",command=self.addincomed)
        transaction.add_command(label="Add Expense",command=self.addexpensed)
        transaction.add_command(label="Registration ",command=self.addreged)
        transaction.add_command(label="Close")
        menubar.add_cascade(label="Transaction", menu=transaction)


        viewmenu=Menu(menubar,tearoff=0)
        viewmenu.add_command(label="View Income",command=self.viewincomed)
        viewmenu.add_command(label="View Expenses",command=self.viewexpensed)
        menubar.add_cascade(label="View",menu=viewmenu)


        reportmenu=Menu(menubar,tearoff=0)
        #reportmenu.add_command(labe"Report",command=self.)

    def homepage(self):
        a=hm.homePage()
        a.root.mainloop()

    def addincomed(self):
        a=ae.addincomeForm()
        a.root.mainloop()

    def addexpensed(self):
        a=exp.addexpenseForm()
        a.root.mainloop()

    def addreged(self):
        a=reg.addregistrationForm()
        a.root.mainloop

    def viewincomed(self):
        a=vi.viewincomeForm()
        a.root.mainloop

    def viewexpensed(self):
        a=ve.viewexpenseForm()
        a.root.mainloop





#main
if __name__ == '__main__':
    MyFrame = MyFrame()
    MyFrame.set_theme("blue")
    MyFrame.mainloop()
