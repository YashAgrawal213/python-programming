x=int(input("enter a number"))
print("all divisors of a number are:")
for k in range(1,x+1):
    if (x%k==0):
        print(k)
