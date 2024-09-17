st = input("enter a string")
occ={}
for i in st:
    count =st.count(i)
    occ[i]=count

print(occ)
