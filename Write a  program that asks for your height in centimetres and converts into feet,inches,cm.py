x=float(input("enter height in centimeters"))
y=x//30.48
x=x%30.48
z=x//2.54
x=x%2.54
print(y,"feet",z,"inches",x,"centimeter")
