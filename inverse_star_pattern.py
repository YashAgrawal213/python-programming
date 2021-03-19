x=int(input("enter the number"))
for i in range (x+1,1,-1):
    for k in range(i,1,-1):
        print("*",end=" ")
        x-=1
    print()
