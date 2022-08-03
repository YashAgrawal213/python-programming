x=int(input("enter price money"))
if x>35000:
    print("discounted price=",x-(x*15/100))
elif x>20000 and x<35000:
    print("discounted price=",x-(x*10/100))
else:
    print("discounted price=",x-(x*5/100))
