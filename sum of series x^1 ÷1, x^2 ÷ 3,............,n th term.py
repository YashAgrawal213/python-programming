x=int(input("enter the number"))
n=int(input("enter range"))
a=1
s=0
for k in range(1,n+1):
    s=s+(x**k/a)
    a=a+2
print(s)
