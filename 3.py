#Write a python program to calculate area of 1O different circles. Given the pie 22/7 and radius of the circles entered by user using Simple Funcbon , 
#Parameterized Function , Return Type with function and retum type With parameterized Functions .


#simple function

def areac():
   pie=22/7
   r=int(input("Enter Radius:"))
   area=round(pie*r*r,2)
   print("Area Is:",area)
for i in range (1,11):
   areac()   

#parameterized 
def areac(r=0):
   pie=22/7
   area=pie*r*r
   print("Area Is:",round(area,2))

for i in range (1,11):
   r=int(input("Enter Radius:"))
   areac(r)   

#return type

def areac():
   pie=22/7
   r=int(input("Enter Radius:"))
   area=round(pie*r*r,2)
   return area

for i in range (1,11):
   ar=areac()
   print("Area Is:",ar)



#parameterized and return
def areac(r):
    pie=22/7
    area=round(pie*r*r,2)
    return area

for i in range (1,11):
    r=int(input("Enter Radius:"))
    a=areac(r)
    print("Area: ",a)

#write a python program to print Multiplication tables from 2 to 20 whether table values entered by user ustng Simple Function , Parameterized Function . 
#Return Type with function and return type with parameterized Functions.

#simple function
def mul():
   
   for i in range(2,21):
      for j in range(1,11):
          print(i,"*",j,"=",i*j)
      print("\n")
mul()

#return type

def multi():
   table=""
   for i in range(2,21):
      for j in range(1,11):
         table+=f"{i} x {j} = {i*j}\n"
      table+="\n"
   return table
table=multi()
print(table)   

   
   


#parameterized
def multiplication(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)

for i in range(2,21):  
 multiplication(i)
 print("\n")

 #parameterized return type
def mult(i,j):
    return i*j
for i in range(2,21):
    for j in range(1,11):
       res=mult(i,j)
       print(i,"*",j,"=",res)
    print("\n")
