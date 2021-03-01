num=input(input("enter your number"))
rev=0
i=num
while i>0:
    rev=(rev*10+num%10)
    num=num//10
if i==rev:
    print("The number is palindrome")
else:
    print("The number is not palindrome")
