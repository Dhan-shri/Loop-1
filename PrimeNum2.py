i=2
f=0
num=int(input("Enter the number"))
while i <(num/2):
    if num%i==0 :
        f=1
        break
    i+=1
if f==0:
    print(num,"It is a Prime Number")
else:
    print(num,"It is a Not Prime Number")