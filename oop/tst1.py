import datetime
class bank:
    bname="sbt"
    #def createAccount(self,bname,accntno,balance):
    def createAccount(self,accntno):
        #self.bname=bname
        self.accntno=accntno
        #self.balance=balance
        self.balance=3000   #minimum balance 3000
    def deposit(self,amt):
        self.balance+=amt
        #print("your",self.bname,"account has been credited with amount",amt)
        print("your",bank.bname, "account has been credited with amount", amt)

        print("on",datetime.datetime.now(),"current balance=",self.balance)
    def withdrw(self,amt):
        if(amt>self.balance):
            print("insufficent balance")
        else:
            self.balance-=amt
        print("your", self.bname, "account has been debited with amount", amt)
        print("on", datetime.datetime.now(), "current balance=",self.balance)
    def balenqiry(self):
        print("your account balance",self.balance)
obj=bank()
#obj.createAccount("sbt",102,2000)
obj.createAccount(102)

obj.balenqiry()
#obj.withdrw(3000)
obj.deposit(1000)
