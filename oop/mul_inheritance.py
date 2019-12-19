class A:
    def m(self):
        print("inside A")
class B(A):
    def m2(self):
        print("inside B")
class c(B):
    def m3(self):
        print("inside C")
od=c()
od.m()
od.m2()
od.m3()

