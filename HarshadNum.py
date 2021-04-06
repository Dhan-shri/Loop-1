num=int(input("Enter the number"))
a=num%10
b=(num//10)%10
c=(num//100)%10
sum=a+b+c
if num%sum==0:
    print("It is a Harshad Number")
else:
    print("it is not Harshad ")