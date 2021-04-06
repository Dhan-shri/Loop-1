i=1
avg=0
sum=0
while i<=11:
    weight=int(input("Enter the Weight"))
    sum=sum+weight
    i=i+1
print(sum)
avg=sum//11
if avg%5==0:
    print(avg,sum,"Its multiples of 5")
else:
    print(avg,"Its not multiple of 5")
    