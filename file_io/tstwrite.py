# f=open('sample one','w')
# lst=["abc","cdc"]
# for item in lst:
#     f.write(item)

# f=open('sample one','r')
# f1=open('sample','w')
# for data in f:
#     f1.write(data)

f=open('/home/luminar/PycharmProjects/luminarpython/file_io/class','r')
fset=set()
for item in f:
    fset.add(item.rstrip('\n'))
print(fset)

f1=open('/home/luminar/PycharmProjects/luminarpython/file_io/fail','r')
f1set=set()
for item in f1:
    f1set.add(item.rstrip('\n'))
print(f1set)
f2set=fset-f1set
f2=open('pass','w')
for item in f2set:
    f2.write(item+ "\n")


