x=int(input("enter present date"))
z=print("""1:january
2: february
3: march
4: april
5: may
6: june
7: july
8: august
9: september
10: october
11: november
12: december""")
y=int(input("enter present month"))
p=28
q=30
r=31
if y==1:
    z=x
elif y==2:
    z=r+x
elif y==3:
    z=r+p+x
elif y==4:
    z=p+(r*2)+x
elif y==5:
    z=p+(r*2)+q+x
elif y==6:
    z=p+(r*3)+q+x
elif y==7:
    z=p+(r*3)+(q*2)+x
elif y==8:
    z=p+(r*4)+(q*2)+x
elif y==9:
    z=p+(r*5)+(q*2)+x
elif y==10:
    z=p+(r*5)+(q*3)+x
elif y==11:
    z=p+(r*6)+(q*3)+x
elif y==12:
    z=p+(r*6)+(q*4)+x
else:
    print("check the input")
print("day of the year =",z)

