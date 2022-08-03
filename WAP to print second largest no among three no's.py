l=[]
for k in range(1,4):
    x=int(input("enter the number"))
    l.append(x)
    l.sort()
print("second largest number:",l[-2])
