num = int(input("Enter our number"))
temp = num
count = 0
arms_num=0

while num>0:
    count = count+1
    num = num//10
print("The count is",count)

while num<0:
    arms_num=(num%10)**count
print("Armstrong number is ",arms_num)