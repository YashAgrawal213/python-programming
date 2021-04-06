z=0
x=int(input("enter the number"))
a=x
while x>0:
    y=x%10
    z=z+y**3
    x=x//10

if z==a:
    print("its an armstrong number")
else:
    print("its not an armstrong number")
