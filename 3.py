#Write a python program to calculate area of 1O different circles. Given the pie 22/7 and radius of the circles entered by user using Simple Funcbon , 
#Parameterized Function , Return Type with function and retum type With parameterized Functions .

def areac(r):
    pie=22/7
    area=pie*r*r
    print("Area: {:.2f} ".format(area))
    return area
for i in range (1,11):
    a=int(input("Enter Radius:"))
    areac(a)

#write a python program to print Multiplication tables from 2 to 20 whether table values entered by user ustng Simple Function , Parameterized Function . 
#Return Type with function and return type with parameterized Functions.

def multiplication(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)

for i in range(1,21):  
 multiplication(i)
 print("\n")