import math
a=float(input("enter value"))
b=float(input("enter value"))
c=float(input("enter value"))
s=(a+b+c)/2
ar=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(ar)
