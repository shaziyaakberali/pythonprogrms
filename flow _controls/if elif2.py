clothtype=int(input("choose cloth type 1.silk 2.linen 3.cotton"))
amount=int(input("enter the amount"))
if(clothtype==1):
    if(amount>=5000):
        print("pay=",(amount-amount*0.12))
    elif(4000<=amount<5000):
        print("pay=",(amount-amount*0.1))
    elif(3000<=amount<4000):
        print("pay=",(amount-amount*0.08))
    else:
        print("pay=",amount)
elif(clothtype==2):
    if (amount >= 5000):
        print("pay=", (amount - amount * 0.2))
    elif (4000 <= amount < 5000):
        print("pay=", (amount - amount * 0.1))
    elif (3000 <= amount < 4000):
        print("pay=", (amount - amount * 0.09))
    else:
        print("pay=", amount-amount*0.05)
elif(clothtype==3):
    if (amount >= 5000):
        print("pay=", (amount - amount * 0.2))
    elif (4000 <= amount < 5000):
        print("pay=", (amount - amount * 0.1))
    elif (3000 <= amount < 4000):
        print("pay=", (amount - amount * 0.09))
    else:
        print("pay=", (amount-amount*0.05))
else:
    print("no offer")
