x=int(input("enter present date"))
print("""1:january
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
if y==2:
    print("number days left =",28-x)
elif y==4 or y==6 or y==9 or y==11:
    print("number days left =",30-x)
else:
    print("number days left =",31-x)
