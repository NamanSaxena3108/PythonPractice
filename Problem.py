i=0
L=[7,1,2,8,0,9]
n=len(L)
while (i<n-1):
    if(L[i] != 0):
        if(i==0):
            i=i+1
        else:
            i=i+L[i]
    else:
        break
if(i==n-1):
    print("true")
else:
    print("false")