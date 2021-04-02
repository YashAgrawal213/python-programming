x=int(input("enter first number"))
y=int(input("enter second number"))
z=int(input("enter third number"))
if x>y and x>z:
    print("the greatest number is:",x)
elif y>x and y>z:
    print("the greatest number is:",y)
else:
    print("the greatest number is:",z)
