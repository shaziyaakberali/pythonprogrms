# f=open('/home/luminar/sample one','r')
# #lst=[]
# for data in f:
#     print(data)

f=open('/home/luminar/sample one','r')
lst=[]
for data in f:
    lst.append(data.rstrip('\n'))
print(lst)