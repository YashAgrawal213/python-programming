n = int(input("enter the last number"))
for k in range(1,n+1,3):
    if k%2==0:
        print(k,end=" ")
    else:
        print(-1*k,end=" ")
