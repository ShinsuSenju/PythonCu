# #Write a program to enter two numbers and perform all arithmetic operations.

# a=int(input("Enter Number 1:"))
# b=int(input("Enter Number 2:"))
# print(a,"+",b"=",(a+b))
# print(a,"-",b"=",(a-b))
# print(a,"*",b"=",(a*b))
# print(a,"/",b"=",(a/b))
# print(a,"%",b"=",(a%b))

# #Write a program to enter marks of five subjects and calculate total and percentage.

# print("Enter Marks Of 5 Subjects")
# a=int(input("Enter Marks In Subject 1:"))
# b=int(input("Enter Marks In Subject 2:"))
# c=int(input("Enter Marks In Subject 3:"))
# d=int(input("Enter Marks In Subject 4:"))
# e=int(input("Enter Marks In Subject 5:"))
# summ=a+b+c+d+e
# print("Total Marks:",summ)
# per=(summ/500)*100
# print("Percentage:",per)

#Write a program to enter length in centimeter and convert it into meter and kilometer, and also convert the same into equivalents.


cm = float(input("Enter length in centimeters: "))
m =cm / 100
km =cm / 100000
print("Length in meters: {:.2f} m".format(m))
print("Length in kilometers: {:.2f} km".format(km))
inches = cm / 2.54
ft = cm / 30.48
yd = cm / 91.44
print("Length in inches: {:.2f} in".format(inches))
print("Length in feet: {:.2f} ft".format(ft))
print("Length in yards: {:.2f} yd".format(yd))
