import matplotlib.pyplot as plt
import pandas as pd
from api import ExpenseTrackerDatabase as db

class showreport():

    def userwisegraph():
        rec=db.userwise_expense()

        print("aft report",rec)



        # listid = []
        # listamount = []
        # for c in rec:
        #     print("Hello")
        #     listid.append(c['_id'])
        #     print(c['_id'])
        #
        #     listamount.append(c['sumamt'])
        #     print(listid)
        #     print(listamount)


        # Creating plot
        fig = plt.figure(figsize=(10, 7))
        plt.pie(rec[1],labels=rec[0])
        #plt.pie(data, labels=cars)

        # show plot
        plt.show()




    def categorywisegraph(self):
        print(" Category wise Data")
        rec = db.categorywise_expense()

showreport.userwisegraph()
