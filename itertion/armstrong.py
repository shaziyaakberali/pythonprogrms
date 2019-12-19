# num=int(input("enter the number"))
# sum=0
# num1=num
# while(num!=0):
#     digit=num%10
#     sum=sum+(digit**3)
#     num=num//10
# print("res",sum)
def arm(num):
    sum=0
    num1=num
    while(num!=0):
        digit=num%10
        sum=sum+(digit**3)
        num=num//10
    print(sum)
arm(23)