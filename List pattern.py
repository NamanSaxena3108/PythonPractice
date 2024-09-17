l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l3=[]
l4=[]
if len(l1) == len(l2):
    for i in range(0,len(l1)):
        l3.append((l1[i]+l2[i]))
print(l3)

for i in range(0,len(l1)):
    l4.append(l1[i])
    l4.append(l2[i])
print(l4)