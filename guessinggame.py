chances=10
number=5
while chances>0:
    num=int(input("Enter the number"))
    if num>chances:
        print("Your guessing number is incorrect")
        chances=num-chances
    elif num==number:
        print("your guessing is correct")
        break
    else:
        print("your number is incorrect")
        chances=chances-num