u=int(input("enter the upper range"))
l=int(input("enter the lower range"))
cE,cO=0,0
for i in  range(l,u+1):
    if i%2==0:
        cE +=1
    else:
        cO +=1

print(cE,cO)