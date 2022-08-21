x=int(input("enter first value"))
y=int(input("enter second value"))
print("choices are")
print("1:ADD  ;  2:SUBTRACT  ;  3:DIVIDE  ;  4:MULTIPLY  ;  5:REMAINDER/MODULUS  ;  6:power")
c=int(input("enter choice"))
if(c==1):
    z=x+y
elif(c==2):
    z=x-y
elif(c==3):
    z=x/y
elif(c==4):
    z=x*y
elif(c==5):
    z=x%y
elif(c==6):
    z=x**y
else:
    print("invalid input")

print(z)