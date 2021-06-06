print("""1=addition
2 =subtraction
3 =multiplication,
4 =division""")
x = input("enter operator needed")
y = int(input("enter first number"))
z = int(input("enter second number"))
if x == "1":
    if y == 56 and z == 9:
        print(y, "+", z, "=77")
    else:
        m = y+z
        print(y, "+", z, "=", m)
elif x == "2":
    m = y-z
    print(y, "-", z, "=", m)
elif x == "3":
    if y == 45 and z == 3:
        print(y, "*", z, "= 555")
    else:
        m = y*z
        print(y, "*", z, "=", m)
elif x == "4":
    if y == 56 and z == 6:
        print(y, "/", z, "=4")
    else:
        m = y/z
        print(y, "/", z, "=", m)
else:
    print("invalid input")

