str=input("enter a string")
c=0
for i in str:
    if i.isalnum():
        c=c+1
print(c)