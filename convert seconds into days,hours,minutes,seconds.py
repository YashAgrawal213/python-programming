s=int(input("enter sec"))
d=s//(24*3600)
s=s%(24*3600)
h=s//(3600)
s=s%3600
m=s//60
s=s%60
print(d,"days",h,"hours",m,"min",s,"sec")
