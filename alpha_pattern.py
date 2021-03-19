x=int(input("enter the number"))
for i in range (1,x+1):
    y=65
    for k in range(1,i+1):
        print(chr(y),end=" ")
        y+=1
    print()
