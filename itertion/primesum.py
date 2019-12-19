rnmin=int(input("enter the range"))
rnmax=int(input("enter the range"))
sum=0
num=rnmin
while(num <= rnmax):
    i=2
    flg=0
while(i<num):
    if(num%i==0):
        flg=flg+1
        break
    #else:
        flg=0
    i+=1
if(flg==0):
    print("prime")
else:
    print("not prime")