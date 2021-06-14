# take statemengt from input funtion and then calculate count of upper characters
# lower chars, special chars, space

# input 
# 'APSSDC Python Programming'

#output
# upper chars are 8, lower are 23, spaces are 3, speciacl chars are 0

u,l,g,s,d = 0,0,0,0,0
string = input('::')
for char in string:
    if char.islower():
        l += 1
    elif char.isupper():
        u += 1
    elif char.isspace():
        g += 1
    elif char.isdigit():
        d += 1
    else:
        s += 1
print('upper chars are {}, lower are {}, spaces are {}, speciacl chars are {}and digits are {}'.format(u,l,g,s, d))
        
