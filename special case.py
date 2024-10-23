#take the number add last 2 digit and divide the original number with the added number and check if it is divisible or not 
n=int(input("Enter a number to check :"))
s=0
a=2
temp1=n
while a != 0:
    temp=temp1%10
    temp1=temp1//10
    s+=temp
    a-=1
if n % s == 0:
    print("Number is divisible")
else:
    print("Number is not divisible")
