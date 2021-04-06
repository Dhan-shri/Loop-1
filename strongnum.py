num=int(input("Enter the Number"))
fact=1
sum=0
a=num
while (a>0):
    digit = a%10
    fact = fact*digit
    sum=sum+fact
    a=a//10
if sum==num:
    print("It is Strong Number")
else:
    print("It is Not a Strong Number")
