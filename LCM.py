num1=int(input("Enter the 1st number"))
num2=int(input("Enter the 2nd number"))
num3=int(input("Enter the 3rd number"))
if ( num1 > num2 and num1 > num3 ):
    maximum_value = num1
    print("The maximum number is",maximum_value)
elif ( num2 > num1 and num2 > num3 ):
    maximum_value = num2
    print("The maximum number is",maximum_value)
else:
    maximum_value = num3
    print("The maximum number is",maximum_value)
while(True):
    if (maximum_value % num1 == 0) and (maximum_value % num2 == 0) and  (maximum_value % num3 == 0) :
        print("LCM is the", maximum_value)
        break
    maximum_value=maximum_value+1