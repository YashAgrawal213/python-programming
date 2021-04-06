x= int(input("enter the number"))
a=0
b=1
s=0
for k in range(x):
    print(s, end=' ')
    a=b
    b=s
    s=a+b
