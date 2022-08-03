x=int(input("enter number between 1-31 :"))
if x>31:
    print("input out of range")
elif x==1 or x==21 or x==31:
    print(x,"st day")
elif x==2 or x==22:
    print(x,"nd day")
elif x==3 or x==23:
    print(x,"rd day")
else:
    print(x,"th day")
