x=int(input("enter the number"))
y=65
for i in range (1,x+1):
    for k in range(1,i+1):
        print(chr(y),end=" ")
        y+=1
    print()
