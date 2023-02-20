#Python program to check whether given number is a palindrome.

n=int(input("Enter number:"))
temp=n
rev=0
while (n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if (temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")


#Python program to check whether enter number is a Armstrong or not

n=int(input("Enter number:"))
temp=n
summ=0
while(n>0):
    rem=n%10
    summ+=rem**3
    n=n//10
if (temp==summ):
    print("The number is a Armstrong Number!")
else:
    print("The number isn't a Armstrong Number!")

#Python program to take three numbers from the user and print the greatest number. 

a=int(input("Enter Number 1:"))
b=int(input("Enter Number 2:"))
c=int(input("Enter Number 3:"))
if (a>b and a>c):
    print("Greatest is ",a)
elif (b>a and b>c):
    print("Greatest is ",b)
else:    
    print("Greatest is ",c)