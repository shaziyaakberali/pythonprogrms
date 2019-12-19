f=open('/home/luminar/Untitled Document 1','r')
lst=[]
for num in f:
    lst.append(num.rstrip('\n'))
    if (num%2==0):
        print(lst)
