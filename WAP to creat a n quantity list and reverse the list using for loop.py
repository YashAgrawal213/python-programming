l =[]
n=int(input("enter number of term to be entered in a list"))
for m in range (1,n+1):
    x=int(input("enter numbers"))
    l.append(x)
for i in range(len(l)-1,-1,-1):
    print(l[i])
