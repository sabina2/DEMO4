num = int(input("Enter our number"))
num1 = num
arms_num = 0

while num>0:
    arms_num = arms_num+(num%10) ** 3
    num=num//10

if arms_num==num1:
    print("Armstrong")
else:
    print("Not Armstrong")



