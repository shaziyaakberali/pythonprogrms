f=open('tmp','r')
dict={}
for item in f:
    data=item.rstrip()
    data=item.split(" ")
    district=data[0]
    tem=data[1]
    print("temp",tem)
    print("district",district)
    if(district not in dict):
        dict[district]=tem
    else:
        old=dict[district]
        if(old<tem):
            dict[district]=tem
        else:
            dict[district]=old
for i in dict:
    print(dict)
    break
f1=open('high','w')
for m,n in dict.items():
    f1.write(m)
    f1.write(n)

