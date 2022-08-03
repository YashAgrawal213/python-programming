print("""use
1 : area of triangle
2 : area of circle
3 : area of rectangle""")
x=int(input("enter choice"))
if x==1:
    b=int(input("enter base"))
    h=int(input("enter height"))
    print("area of triangle",0.5*b*h)
elif x==2:
    r=int(input("enter radius"))
    pi=3.14
    print("area of circle",pi*r*r)
elif x==3:
    b=int(input("enter base"))
    l=int(input("enter length"))
    print("area of rectangle",l*b)
else:
    print("invalid input")
