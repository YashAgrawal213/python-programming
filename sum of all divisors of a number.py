c=0
x=int(input("enter a number"))
print("sum all divisors of a number is:")
for k in range(1,x+1):
    if (x%k==0):
        c=c+k
print(c)
