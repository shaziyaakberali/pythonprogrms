# lst=[10,20,30,40]
# sum=0
# for item in lst:
#     squ=item**2
#     print(squ)
lst=[10,20,30,40]
flg=0
num=int(input("enter the number"))
for item in lst:
    if(item==num):
        flg+=1
        break
    else:
        flg=0
if(flg>0):
        print("elemenrt found")
else:
    ()
