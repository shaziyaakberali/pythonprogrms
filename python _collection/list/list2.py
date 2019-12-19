# lst=[]
# cnt=int(input("enter the length"))
# for i in range(0,cnt):
#     element=int(input("enter the elements"))
#     lst.append(element)
# print

lst=[]
lstevn=[]
lstodd=[]
cnt=int(input("enter the length"))
for i in range(0,cnt):
    element=int(input("enter the elements"))
    #lst.append(element)
    if(element%2==0):
        lstevn.append(element)
    else:
        lstodd.append(element)
print("lstevn=",lstevn)
print(lstodd)

