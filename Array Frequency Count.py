import array as ar
a=ar.array('i',[1,7,4,0,1,2,7,4,7,7,2,0])

for i in a:
    count=a.count(i)
    print(f"{i}   {count}")
    while i in a:
        a.remove(i)