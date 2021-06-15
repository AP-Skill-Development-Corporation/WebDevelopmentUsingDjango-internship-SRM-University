#list is not a homogeneous array.
l = [1,2,2.4,5.7, 'a','b',['a',4,6]]
print(l, type(l))


# list has type indexing
# positive index: 0,..,n-1    (n - is length of the list)
# negative index:-n,-n-1,..-1
print('l[3] :', l[3]) # 5.7
print('l[-2] :',l[-2])
print('l[-1][1] :',l[-1][1]) # 4


# what does mutability in list
l[1] = 1000
print(l) 


# use slicing for list.
# [start:end:step]
print(l[1::])
print(l[-1::-1])# -1 -2 -3
print(l[::-1])
