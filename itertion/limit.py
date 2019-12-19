rnmin=int(input("enter the value"))
rnmax=int(input("enter the value"))
sum=0
while (rnmin<=rnmax):
    if(rnmin%2 ==0):
        sum=sum+rnmin
    rnmin+=1
print(sum)