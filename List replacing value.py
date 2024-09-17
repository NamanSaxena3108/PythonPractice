l=[1,2,3,4,5]
old=3
new=6
if old in l:
    i=l.index(old)
    l[i]=new
print(l)