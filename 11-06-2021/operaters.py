# Operators
# 1. Arithmetic operators
# 2. Assignement operators
# 3. Comparison operators
# 4. Logical Operators
# 5. Membership Operators
# 6. Bitwise Operators


# Arithmetic Operators(+,-,*,/,//,**)
print("Arithmetic Operators(+,-,*,/,//,**)")
a = 2
b = 3

print('Addition: ',a+b)
print('Subtraction: ',a-b)
print('Multiplication: ',a*b)
print('Division: ',a/b)
print('Floor Division: ',a//b)
print('Exponentiation: ',a**b)

# Assignement operators(=,+=,-=,*=,/=)
print("Assignement operators(=,+=,-=,*=,/=)")
number = 1
print(number)
number += 1 # number = number+1, number = 1+1 = 2
number += 5 # number = number+5, number = 2+5 = 7
print(number)

number -= 3 # number = number-3
print(number)

number *= 10 # number = number*10
print(number) # number =40

number /= 10 # number  = number/10
print(number)  # number = 4.0

var = 12.23348348
new_var = round(var,2)
print(new_var)
print(round(12.2856,2))


# comparison operators(==,!=, >=, <=,>, <)
# It return either true or false
print("Comparison Operators(==,!=, >=, <=,>, <)")
print(a==b)
print(True==-1)
print("Greater than >: ",a>b)
print("Less than <: ",a<b)
# a<=b -> if a<b= True or if a=b True
print(a<=b)
print(2<=2)
result = 2!=3
print(result)
print(2==3)


# Logical Operators (and, or, not)
print("Logical Operators (and, or, not)")
a=3
b=5

statement1 = a<b #(True)
statement2 = a>=b # False

result = statement1 and statement2
print(result) # false
result2 = statement1 or statement2 # true or false
print(result2)

print(not(True))
print(not("asfadfad"))

print(not(a>=b))


