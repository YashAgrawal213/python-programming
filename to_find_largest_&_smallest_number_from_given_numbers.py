x= int(input("enter the frequency of numbers "))
z=[]
for k in range(1,x+1):
    y=int(input("enter the numbers"))
    z.append(y)
z.sort()
print("largest number is:",z[-1])
print("smallest number is:",z[0])
