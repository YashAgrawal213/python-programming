c=0
x=int(input("enter a number"))
print("number of divisors of a number are:")
for k in range(1,x+1):
    if (x%k==0):
        c=c+1
print(c)
