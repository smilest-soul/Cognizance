S=int(input("Enter your number"))
m=S
sum=0
while(S>0):
    rem=S%10
    sum=sum*10+rem
    S=S//10
if(m==sum):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")