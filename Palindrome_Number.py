num=int(input("Enter your number"))
tem=num
rev=0

while num>0:
    rev=rev*10+num%10
    num=num//10

if tem==rev:
    print("Palindrome")
else:
    print("Not Palindrome")