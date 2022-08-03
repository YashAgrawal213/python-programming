x=int(input("enter any number"))
c=0
d=0
while x>0:
    y=x%10
    if y%2==0:
        c=c+y
        x=x//10
    else:
        d=d+y
        x=x//10
print("sum odd digits is =",d)
print("sum even digits is =",c)
