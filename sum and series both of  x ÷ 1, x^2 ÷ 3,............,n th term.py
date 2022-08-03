a=1
b=0
x=int(input("enter the number"))
n=int(input("enter range"))
print("series:")
for k in range(1,n+1):
    m=(x**k)/a
    print(m,end=" ")
    a=a+2
    b=b+m
print()
print()
print("sum of series = ",b)
