x=int(input("enter marks"))
y=int(input("enter marks"))
z=int(input("enter marks"))
a=int(input("enter marks"))
b=int(input("enter marks"))
t=a+b+x+y+z
print("total marks=",t)
p=t*100/500
print("percentage =",p,"%")
if p>=85:
    print("Grade : S")
elif p>=75 and p<85:
    print("Grade : A")
elif p>=60 and p<75:
    print("Grade : B")
elif p>=50 and p<60:
    print("Grade : C")
else:
    print("Grade : F")
    
