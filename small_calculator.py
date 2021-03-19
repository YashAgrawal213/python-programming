x=int(input("enter first number"))
y=int(input("enter second number"))

print('''1:add
         2:subtract
         3:multiply
         4:divide ''')
c=int(input("enter choice"))

if c==1:
    print("sum",x+y)
elif c==2:
    print("subtract",x-y)
elif c==3:
    print("multiply",x*y)
elif c==4:
    print("divide",x/y)
else:
    print("invalid input")
