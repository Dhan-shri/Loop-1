# Strong Number

num=int(input("Enter a number"))
sum=0
a=num
while (a):
    i=1
    fact=1
    rem=a%10
    while(i<=rem):
        fact=fact*i
        i=i+1
    sum=sum+fact
    a=a//10
if sum==num:
    print("Given number is Strong number")
else:
    print("Given number is not Strong number")
