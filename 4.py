#Program to demonstrate the various kind of operations that can be applied to the string.

#1 Python program to check whether the string is Symmetrical or Palindrome
def ispal(s):
    return s == s[::-1]

def issym(s):
    n = len(s)
    if n % 2 == 0:
        return s[:n//2] == s[n//2:][::-1]
    else:
        return s[:n//2] == s[n//2+1:][::-1]

string=input("Enter A String")
if(ispal(string)):
    print("Palindrome")
if(issym(string)):
    print("symmetrical")
else:
    print("None")    


#2 Python program to find uncommon words from two Strings
str1=input("Enter String 1")
str2=input("Enter String 2")
s1 = str1.split()
s2 = str2.split()
uncommonWords = ''
for words in s1:
    if words not in s2:
        uncommonWords = uncommonWords+" "+words
for words in s2:
   if words not in s1:
        uncommonWords = uncommonWords+" "+words
  
print("All uncommon words from both the string are:",uncommonWords)

#3 Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 
# 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Example:- Sample String : 'abc' 
# Expected Result : 'abcing' Sample String : 'string' Expected Result : 'stringly'

string=input("Enter A Word:")
n=len(string)
if n<3:
    print(string)
elif string[-3:]=="ing":
    string+="ly"
    print(string)
else:
    string+="ing"
    print(string)    



