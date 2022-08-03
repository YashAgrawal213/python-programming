n = int(input("enter the last number"))
for i in range(1,n):
    j=i*i+5
    if j<=n:
        print(j,end=" ")
    else:
        break
