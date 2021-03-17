x=int(input("enter the number"))
c=0
for k in range(1,x+1):
    if x%k==0:
        c=c+1
if c==2:
    print("Prime number")
else:
    print("Not A Prime Number")
