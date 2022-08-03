x=int(input("enter any number"))
c=0
while x>0:
    y=x%10
    c=c+(y**2)
    x=x//10
print("sum of square of digits is =",c)
