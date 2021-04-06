n=int(input("Enter the number"))
s=0
i=1
while i < n :
    if n%i == 0 :
        s=s+1
    i=i+1
if s==n:
    print("perfect number")
else:
    print("Not a perfect number")
