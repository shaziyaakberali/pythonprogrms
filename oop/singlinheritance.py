# single inheritance
class base:
    def m(self):
        print("inside base class")
class derived(base):    #inheritance
    def m2(self):
        print("inside derived")
ob=derived()
ob.m2()
ob.m()

#method overriding:same method signture (name of method+argument)for baseclas and derived class

class base:
    def m(self):
        print("inside base class")
class derived(base):
    def m(self):
        print("inside derived")
ob=derived()
ob.m()