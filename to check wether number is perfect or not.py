s=0
x=int(input("enter a number"))
for k in range(1,x):
    if (x%k==0):
        s=s+k
        
if s==x:
    print("perfect number")
else:
    print("not a perfect number")
