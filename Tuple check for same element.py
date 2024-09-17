tup=(10,10,10,10,10)
same=all(x==tup[0] for x in tup)
if same:
    print("same")
else:
    print("not same ")