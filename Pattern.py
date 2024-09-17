a,b,i,j,flag=0,0,0,0,0
print("enter upper limit")
a=int(input())
print("enetr the lower limti")
b=int(input())
for i in range(a,b+1):
    if (i==0):
        continue
    flag=1
    for j in range(2,i//2 +1):
        if(i%j==0):
            flag=0
            break
    if(flag==0):
        print(i,end=" ")
        