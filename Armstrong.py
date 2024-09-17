n=int(input("enter the number"))
s=0 ; a=n
while a!=0:
    d=a%10
    s=s+(d*d*d)
    a=a//10
if(s==n):
    print("armstrong")
else:
    print("not")