c=1
l=2
n=int(input("enter n term"))
for k in range(1,n+1):
    print(c,end=" ")
    c=c*10+l
    l=l+1
