# 2 is the even number which is prime number
number = int(input("Please enter any number:"))
count = 0
i=2
while i<number:
    if number % i == 0 :
        print(number,"number is not prime")
        break
    i+=1
else :
    print(number,"number is prime number")
    