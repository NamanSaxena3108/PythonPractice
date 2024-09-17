st=input("enter a string")
for i in st:
    if i.isalnum() == False:
        st = st.replace(i,"@")
print(st)