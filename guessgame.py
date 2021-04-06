# fix_number=5
# chances=10
# while chances>0:
#     diff=0
#     number=int(input("Guess the number"))
#     if fix_number==number:
#         print("Your Guessing number is correct !!")
#         break
#     elif (number>chances) or (number>fix_number) :
#         diff=number-fix_number
#         chances=chances-diff
#         print("remaining your chances",chances)
#     elif number<=chances:
#         diff=fix_number-number
#         chances=chances-diff
#         print("Remaining your chances",chances)
#     else:
#         print("Your guessing number chances finished ! Try again ")

print("WELCOME THE GUESSING GAME WORLD ")
fix_number=5
chances=10
while chances>0:
    diff=0
    number=int(input("Guess the number to win the game:-"))
    if fix_number==number:
        print("Your Guessing number is correct,, You are Win !!")
        break
    elif number>fix_number:
        diff=number-fix_number
        chances=chances-diff
        if chances<0:
            print("chances finished")
            break
        else:
            print("Remaining chances have left",chances)
    elif number<fix_number:
        diff=fix_number-number
        chances=chances-diff
        if chances<0:
            print("chances finished")
            break
        else:
            print("remaining chances",chances)
    else:
        print("Your guessing number chances finished ! Try again ")

