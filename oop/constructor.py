class student:
    clgname="luminar"
    def __init__(self,st_name,id):
        self.st_name=st_name
        self.id=id
    def printVal(self):
        print("name=",self.st_name)
        print("id=",self.id)
st=student("ajay",1)
st2=student("vijay",2)
st.printVal()