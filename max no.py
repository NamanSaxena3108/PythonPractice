l=[1,2,4,6,8,-1,10,20,-4,3,1,50,-70]
u=0
t=0
for i in l:
    if i>0:
        u+=i
    elif u>t:
        t=u
        u=0
print(t)
    