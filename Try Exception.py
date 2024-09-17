try:
    l=[10,20,30,40,50]
    item=int(input("enter the number after we will insert"))
    data=int(input("enter the number to be inserted"))
    index=l.index(item)
    l.insert(index+1,data)
    print(l)
except Exception as e:
    print(e)
finally:
    print("program done")
