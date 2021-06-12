# Strings : A sequence of characters is called a string
# we represent a string with single/double quotes("",'')
# Strings are ordered and Iterable

s = "Python"
s1 = "srmap"
s2 = "SrmAP"
a=4

print(s[3])
# len(): To get the length of the string
print(len(s))
# dir(): To get all the methods available
print(dir(s))
# capitalize()
print("Capitalize():",s1.capitalize())
print("upper():",s.upper())
print("lower():",s.lower())
print("casefold():",s1.casefold()==s2.casefold())
print("isupper():",s.isupper())
print("islower():",s.islower())
print("index():",s.index("h"))
print("replace():",s.replace("t","T"))

# Negative Indexing:
print(s[-3])
# Slicing

s = "python Programming srmap"
s1 = ""
s1 = s1+s[0]
s1 = s1+s[1]
s1 = s1+s[2]
s1 +=s[4]
print(s1)


s2 = s[0:6]
print(s2)
print(s[1:6])
print("All the chars:",s[:])
print(s[4:])
print(s[5:8])# s[5],s[6],s[7]
print(s[15:]) 
print(s[-3:])
print(s[0:6:1])
print(s[0:6:2])
print(s[::3]) #ph oai m
print(s[-1:-5:-2])#-1, -1-2 = -3, -3-2 = -5
print(s[-1::-1]) #-1, -1-1=-2,-2-1 = -3,...
print(s[::3]) #ph 






      
