import array as ar
a=ar.array('i',[10,20,30,20,30,10,20,20])
dic={}
for i in a:
    c=a.count(i)
    dic[i]=c
print(dic)