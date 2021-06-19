# Lambda : Anonymous function(funtion without name)
# It can contain one or more number of arguments but a single expresion
# lambda arguments(x,y,..):expression


# input : n
# output : n**2


lam = lambda n,a:n*a


print(lam(5,2))


# list = [1,2,3,4,5]
# ouput : [2,3,4,5,6]

x = lambda x:x+1


print(list(map(x,[1,2,3,4,5])))
# if n is even : return n**2
# else : return n**3
# [1,2,3,4]
# [1,4,27,16]

l = list(range(1,11))
# lambda with if-else : lambda n:n if n%2==0 else 0

even = lambda n: n**2 if n%2==0 else n**3

evens = list(map(even,l))
print(evens)


# Filter
# filter() is a function which takes a funtion and a sequence and return all the true cases


#program to get even numbers in a list by using filter


l = [12,23,34,10,1]

def even(n):
    if n%2==0:
        return True
    return False

result = list(filter(even,l))
print(result)

print(list(filter(lambda x:True if x%2==0 else False, l)))





















