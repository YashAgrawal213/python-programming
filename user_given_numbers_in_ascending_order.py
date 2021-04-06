y=[]
n=int(input("enter range of integer quantities"))
for k in range(1,n+1):
    x=int(input("enter the integers"))
    y.append(x)
y.sort()
print("In Ascending order",y)
