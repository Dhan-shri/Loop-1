num=int(input("Enter the number"))
num_1 =num%10
num_2 = (num//10)%10
num_3 =(num//100)%10
num_4 =(num//1000)%10
new_num = ((num_1*1000))+(num_2*100)+(num_3*10)+(num_4)
if num<10000:
    print(new_num)
else:
    print("It is not new Number")