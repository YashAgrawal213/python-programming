a=2
n=int(input("enter range"))
print("series:")
for k in range(1,n+1):
    
    if k%2==0:
        print("- (x ^",k,"/",a,")",end=" + ")
        a=a+1
        
    else:
        print("(x ^",k,"/",a,")",end=" ")
        a=a+1
        
