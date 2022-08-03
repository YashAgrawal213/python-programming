x=int(input("enter weight of the product"))
while (x>10):
    y=x//10
    x=x%10
if x>0:
    print("courier charges =",(y+1)*2)
else:
    print("courier charges =",(y)*2)
