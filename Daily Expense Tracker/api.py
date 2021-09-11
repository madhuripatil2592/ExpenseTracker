from pymongo import MongoClient
import  datetime
import user as u
try:
    con=MongoClient()
    print("Connected Successfully")
except:
    print("Cant connect to Mongodb")

db=con.expensetracker
#tab=db.login
reg=db.register
income=db.income
exp=db.expense

class ExpenseTrackerDatabase():


    def chk_login(user,passwd):
        print("user=",user)
        print("pwd=",passwd)
        q1={ "$and": [{"username":user}, {"password":passwd}]}
        print(q1)
        DATA=db.register.find(q1)

        print("FROM API: retrived rows :", DATA.count())
        if(DATA.count() > 0):
            print(DATA)
            for rec in DATA:
                print(rec['id'])
                uid=rec['id']
                uname=rec['username']
                fname=rec['first']
                print(" api id,uname",uid,uname,fname)
                #obj=u.User("11","sdfs")
                uobj=u.User(str(uid),str(uname),str(fname))
            return  uobj# user pw is correct
        else:
            return 0 #user pw wrong








    def add_register(fname,mname,lname,gender,email,contact,city,address,username,password):
        getid=db.register.find()
        newid=getid.count()+1


        print("fname=",fname)
        data={'id':newid,'first': fname,
                        'middle': mname,
                        'last':lname,
                        'gender':gender,
                        'mail':email,
                        'contact':contact,
                        'city':city,
                        'address':address,
                        'username':username,
                        'password':password}
        print("Insert data=",data)
        x=reg.insert_one(data)



    def add_income(uid,amt,source,date):
        getid = db.income.find()
        newid = getid.count() + 1
        #NOTES :: DATE WE PASSING AS PARAMTER HERE BUT NOT USING,
        #WE ARE ADDING MONGODB DATE INTO TABLE
        #SO THAT IS USED TO COMPAIRE MONTH N YEAR
        #db.income.insert({'date': new Date()})
        data={'tid': newid, 'uid': uid,'amount':amt,'source':source,'DATE':datetime.datetime.today().replace(microsecond=0)}
        print("INSERT=",data)
        x=income.insert_one(data)

    def add_expense(tid,uid,uname,amt,source,category,mode,d):
        data={'tid':tid,'uid':uid,'amount':amt,'username':uname,'source':source,'category':category,'paymode':mode,'DATE':datetime.datetime.today().replace(microsecond=0)}
        x=exp.insert_one(data)
        print("insert",data)

    def view_totalincome(cmonth,cyear):
        q1={"$and" : [{ "$expr": { "$eq": [{ "$month": "$DATE"  }, int(cmonth)] }},{ "$expr": { "$eq": [{ "$year": "$DATE"  }, int(cyear)] }}]}
        print(q1)
        DATA=db.income.find(q1)
        print("FROM API: retrived rows:",DATA.count())
        return DATA



    def view_income(pmonth,pyear):
        print("month=",pmonth)
       # q={ "$expr": { "$eq": [{ "$month": "$DATE"  }, int(pmonth)] }}
        q1={"$and" : [{ "$expr": { "$eq": [{ "$month": "$DATE"  }, int(pmonth)] }},{ "$expr": { "$eq": [{ "$year": "$DATE"  }, int(pyear)] }}]}
        print( q1)
        DATA=db.income.find(q1)
        print("FROM API: retrived rows :", DATA.count())

        #data=income.find({})
        return DATA

    def view_expense(pmonth,pyear):
        q2={"$and" : [{ "$expr": {"$eq":  [{ "$month" : "$DATE" }, int(pmonth)] }},{ "$expr": {"$eq": [{ "$year": "$DATE" }, int(pyear)]  }} ]}
        print(q2)
        DATA=db.expense.find(q2)
        print("FROM API:retrived rows:",DATA.count())
        return DATA


    def categorywise_expense():
        cur=db.expense.aggregate([{"$group":{"_cat":"$category","total":{"$sum": "$amount"}}}])
        listcat=[]
        listamount=[]
        report=[]
        for c in cur:
            print("Hello")
            listcat.append(c['_cat'])
            print(c['_cat'])


        



    def userwise_expense():
        cur=db.expense.aggregate([{"$group":{"_id":"$uid","sumamt":{"$sum":"$amount"}}}])

        #return cur
        listid = []
        listamount = []
        report = []
        for c in cur:
            listid.append(c['_id'])
            print(c['_id'])


            listamount.append(c['sumamt'])
            print(listid)
            print(listamount)

        report.append(listid)
        report.append(listamount)
        print("bef rep : ",report)
        return report
            #print(self.listsumamt)


    def getmaxtid(self):
        self.maxtid=''
        cur=db.expense.aggregate([{"$group":{"_id":"null","MaximumValue":{"$max":"$tid"}}}])
        print(cur)
        for c in cur:
            self.maxtid=c['MaximumValue']
            print(c)
            print("Maximum Value of Tid",self.maxtid)
        return self.maxtid


    def income_expense_curve(year,month):
        pass
    def view_balance(tot_income,tot_exp,savings,date):
        pass
#ExpenseTrackerDatabase.userwise_expense()
#e.chk_login()self
#ExpenseTrackerDatabase.find_id()
ExpenseTrackerDatabase.userwise_expense()
#e.getmaxtid()
#e.userwise_expense()
