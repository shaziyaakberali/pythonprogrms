lst=[10,20,50,40,5]
lst=sorted(lst)
print(lst)
flag=0
low=0
upper=len(lst)
mid=(low+upper)//2
elemnt=int(input("enter the elements"))
while(low<=upper):
    if(elemnt>lst[mid]):
        low=mid+1
    elif(elemnt<lst[mid]):
        upper=mid-1
    elif(elemnt==lst[mid]):
        flag+=1
        break
    mid=(low+upper)//2
if(flag>0):
    print("elemnt found ")
else:
    print("not found")




