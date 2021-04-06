num1=int(input("Enter the 1st number"))
num2=int(input("Enter the 2nd number"))
if num1>num2:
    max1=num1
    print("the maximum num",max1)
else :
    max1=num2
    print("the maximum num",max1)
if num1<num2:
    min1=num1
    print("the minimum num",min1)
else :
    min1=num2
    print("the minimum num",min1)
while max1%min1!=0:
    rem=max1%min1
    max1=min1
    min1=rem
print("HCf is",min1)