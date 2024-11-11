s = input("Enter a String")
a = ""
for i in s:
    if i.isalpha():
        a+=i
    elif i.isdigit():
        a+=i
    elif i.isspace():
        a+=i
    else:
        continue
print(a)        