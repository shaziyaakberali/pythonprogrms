mark1= int(input("sub 1 mark="))
mark2=int(input("sub2 mark ="))
mark3=int(input("sub3 mark ="))
total=(mark1+mark2+mark3)

if(total>140):
    print("grade is A+")
elif(total>=140 and total>130):
    print("grade is A")
elif(total>=130 and total>120):
    print("grade is B+")
elif(total>=120 and total>110):
    print("grade is B")
else:
    print("fail")
