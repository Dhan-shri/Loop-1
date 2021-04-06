week = int(input("Enter the week"))
while week <=7 :
    day=input("Enter the morning/afternoon/evening")
    if day == 'morning':
        print("It is Excercise")
        continue
    elif day == 'afternoon' :
        print("It is a Cultural activity")
        continue
    elif day == 'evening':
        print("It is a Study Time")
        continue
    else :
        print("Enter the correct day of time")
    week+=1
else:
    print("Try to make your New Schedule for 7 Days")