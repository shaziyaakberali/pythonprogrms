class student:
    schoolname="luminar"
    def setval(self,id,name):
        self.id=id
        self.name=name
    def printval(self):
        print(self.id,"==",self.name,"==",student.schoolname)
    @classmethod
    def setschool(cls,name):
        cls.name=name
    @staticmethod
    def greetings():
        print('welcome')
s=student()
s.setval(100,"noname")
s.printval()
s.setschool("lumimar techno lab")
s.printval()
student.greetings()