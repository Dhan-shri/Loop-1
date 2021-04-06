num=int(input("Enter the number"))
row=0
while num>0:
    star=num
    while star>0:
        print(" * ", end=" ")
        star=star-1
    space=num-row-1
    while space>0:
        print(" ",end="")
        space=space-1
print()
row=row+1