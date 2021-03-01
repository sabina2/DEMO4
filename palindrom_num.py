num=int(input("enter your number"))
i=num
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10
if rev==i:
    print("Palinrome")
else:
    print("Not palindrome")