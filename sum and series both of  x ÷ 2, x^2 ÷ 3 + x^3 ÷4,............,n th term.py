a=2
b=0
x=int(input("enter the number"))
n=int(input("enter range"))
print("series:")
for k in range(1,n+1):
    m=(x**k)/a
    if k%2==0:
        print(-m,end=" ")
        a=a+1
        b=b+m
    else:
        print(m,end=" ")
        a=a+1
        b=b+m

print()

print()
print("sum of series = ",b)
