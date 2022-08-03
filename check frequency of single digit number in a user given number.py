x=0
c=0
n=int(input("enter a number "))
a=int(input("enter a number whose frequency to be checked"))
while n>0:
    x=n%10
    if x==a:
        c=c+1
    n=n//10
print("frequency of",a,"=",c)
 
