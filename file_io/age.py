import operator
f=open('/home/luminar/PycharmProjects/luminarpython/file_io/fakefriends.csv','r')
dict={}
for item in f:
    item=item.rstrip()
    data=item.split(",")
    name=data[1]
    age=data[2]
    print("name=",name)
    print("age=",age)
    if(age not in dict):
        dict[age]=1
    else:
        dict[age]+=1
#print(dict)


    sorted_d=sorted(dict.items(),key=operator.itemgetter(0))
print(sorted_d)
#print(sorted_d[0])





