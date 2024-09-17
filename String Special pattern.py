st=input("enter a string")
s, avg, count = 0, 0, 0
for i in st:
    if (i.isdigit() == True):
        count += 1
        s = s+int(i)
        avg=s//count

print(count,s,avg)
