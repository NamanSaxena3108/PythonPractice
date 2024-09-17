s1={10,20,37,50}
s2={60,65,40,30}
l1=list(s1)
l2=list(s2)
c=0
for i in l1:
    if i in l2:
        c+=1
        print(i)
if c==0:
    print("No common elements")