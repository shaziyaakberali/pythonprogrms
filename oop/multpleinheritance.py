# class parent1:
#     def m1(self):
#         print("inside parent1")
# class parent2:
#     def m2(self):
#         print("inside parent2")
# class child(parent1,parent2):
#     def m3(self):
#         print("inside child")
# c=child()
# c.m3()
# c.m2()
# c.m1()

#invoke according to priority
class parent1:
    def m1(self):
        print("inside parent1")
class parent2:
    def m1(self):
        print("inside parent2")
class child(parent1,parent2):
    def m3(self):
        print("inside child")
c=child()
c.m3()

c.m1()