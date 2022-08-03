l =[]
n=int(input("enter number of term to be entered in a list"))
for m in range (1,n+1):
    x=int(input("enter numbers"))
    l.append(x)
print(l)
print("reversed list:",l[::-1])
