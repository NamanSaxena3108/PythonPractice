u=int(input("enter the upper limit"))
l=int(input("enter the lower limit"))
s=0
for i in range(l,u+1):
    if(i%2 != 0):
        s=s+i

print(i)