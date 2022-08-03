print("if bill price exceeds RS 10000 then 5% discounted price will be provided")
x=float(input("enter rate of product"))
y=int(input("enter quantity of product"))
t=x*y
if t>10000:
    print("total amount=",t-(t*5/100))
else:
    print("total amount=",t)
