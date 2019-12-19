f=open('/home/luminar/PycharmProjects/luminarpython/file_io/txt')
lst=[]
dict={}
for item in f:
    #lst=item
    print(item)
    lst.append(item.rstrip('\n'))
    print(lst)
#print(lst)
for word in lst:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
f1=open('word','w')
for i,j in dict.items():
    i=str(i)
    j=str(j)
    f1.write(i)
    f1.write("/t")
    f1.write(j)

