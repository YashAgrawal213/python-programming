x=int(input("enter the number"))
i=2
while x!=1:
    if x%i==0:
        print(i,end=" * ")
        x=x/i
    else:
        i=i+1
print("1")
