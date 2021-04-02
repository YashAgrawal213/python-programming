r=float(input("enter radius of circle"))
print('''1: For AREA
2: For PERIMETER''')
c=float(input("enter choice"))
if c==1:
    print("AREA OF CIRCLE =",(3.14159*(r**2)))
else:
    print("PERIMETER OF CIRCLE =",(2*3.14159*r))
