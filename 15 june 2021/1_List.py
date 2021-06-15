# define with []
# l = [1,2,3,4,5]
# print(type(l))

# a = list(1,2,3,4)
# TypeError: list expected at most 1 argument, got 4
# print(type(a),a)

# a = list([1,2,3,4]) #list((1,2,3,4))
# print(type(a),a)

# it will create a empty list
#b = list()
#print(type(b),b)

# we can also create a empty list by using []


# converting a string into list
#string = 'python'
#list_str = list(string)
#print('converted string', list_str)

# we can not convert a string to list
#string = 'python'
#str_to_list = [string]
#print(str_to_list, type(str_to_list))

# by using string method we can convert string to list
string = 'python'
str_list = string.split('t')
print(str_list, type(str_list))

