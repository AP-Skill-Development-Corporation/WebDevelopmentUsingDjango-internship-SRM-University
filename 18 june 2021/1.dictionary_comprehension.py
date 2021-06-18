# create a dict of n numbers with values squares of that number

#n = int(input("enter n:"))

# set comprehension
#result = {i**2 for i in range(1,n+1)}
# dictionary comprehension
#dict_result = {i:i**2 for i in range(1,n+1)}
#print(dict_result)

#Welcome to Web Development Using Django internship this repository consists of all the files

n = 'Welcome to Web Development Using Django'

m = {i.upper():i for i in n.split()}
print(m)
