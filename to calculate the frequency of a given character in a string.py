x=input("enter string")
c=0
y=input("enter character whose frequency to be searched")
for k in x:
    if k==y:
        c=c+1
    else:
        continue
print(k,":",c)
