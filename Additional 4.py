#1.Find Number Of Vowels In String. 
#2.Convert Lower Case to Upper And Vice-Versa
#3.Find No of Lines, spaces and consider digits as blank spaces

def countn(str):
    cn=0;
    for i in str:
        if i=="\n":
            cn=cn+1
    return cn

def isalpha(s):
    st=ord(s)
    if(st<65 and st>90 or st<95 and st>122):
        return 1
    else:
        return 0

def counts(str):
    cs=0
    for i in str:
        if i==" " or i in '123456789':
            cs=cs+1        
    return cs

def countv(str):
    cv=0
    for i in str:
        if i in 'aeiouAEIOU':
            cv+=1
    return cv

def conv(str):
    s=""
    for i in str:
        ch=ord(i)
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            s=s+chr(ord(i)+32)
        elif i in 'abcdefghijklmnopqrstuvwxyz':
            s=s+chr(ord(i)-32)
        else:
            s=s+i  
    return s

str="""PyTHon 
 is 
    very cool123"""
newlines=countn(str)
space=counts(str)
vowel=countv(str)
nstr=conv(str)
print("Spaces:",space,"\nNewlines:",newlines,"\nVowels:",vowel,"\nString After Conversion is:"+nstr)                         

#2
string = "hello world"

# Method 1: startswith()
print(string.startswith("hello"))

# Method 1 without built-in function
def startswith(string, prefix):
    return string[:len(prefix)] == prefix

print(startswith(string, "hello"))



# Method 2: upper()
print(string.upper())

# Method 2 without built-in function
def upper(string):
    result = ""
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

print(upper(string))

# Method 3: lower()
print(string.lower())

# Method 3 without built-in function
def lower(string):
    result = ""
    for char in string:
        if ord(char) >= 65 and ord(char) <= 90:
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

print(lower(string))

# Method 4: count()
print(string.count('l'))

# Method 4 without built-in function
def count(string, char):
    result = 0
    for c in string:
        if c == char:
            result += 1
    return result

print(count(string, 'l'))

# Method 5: replace()
print(string.replace('o', 'a'))

# Method 5 without built-in function
def replace(string, old, new):
    result = ""
    for char in string:
        if char == old:
            result += new
        else:
            result += char
    return result

print(replace(string, 'o', 'a'))

# Method 6: join()
words = ["Hello", "World"]
print("-".join(words))

# Method 6 without built-in function
def join(separator, words):
    if len(words) == 0:
        return ""
    result = words[0]
    for word in words[1:]:
        result += separator + word
    return result

print(join("-", words))


# Method 7: isalpha()
print(string.isalpha())

# Method 7 without built-in function
def isalpha(string):
    for char in string:
        if not (ord(char) >= 65 and ord(char) <= 90) and not (ord(char) >= 97 and ord(char) <= 122):
            return False
    return True

print(isalpha(string))

# Method 8: isnumeric()
print(string.isnumeric())

# Method 8 without built-in function
def isnumeric(string):
    for char in string:
        if not (ord(char) >= 48 and ord(char) <= 57):
            return False
    return True

print(isnumeric(string))

# Method 9: index()
print(string.index('w'))

# Method 9 without built-in function
def index(string, char):
    for i in range(len(string)):
        if string[i] == char:
            return i
    return -1

print(index(string, 'w'))

# Method 10: split()
string="Python is Very Very Cool"
s=string.split()
print(s)

# Method 10 without built-in function
string="Python is Very Very Cool"
space=" "
word=""
result=[]
i=0

while i < len(string):
    if string[i] == space:
        result.append(word)
        word = ""
    else:
        word += string[i]
    i+= 1

result.append(word) 
print(result)




