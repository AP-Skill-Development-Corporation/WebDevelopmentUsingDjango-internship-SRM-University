#'append', 'clear', 'copy', 'count', 'extend',
#'index', 'insert', 'pop',
#'remove', 'reverse', 'sort'

L = [1,2,3,4,3]
# append 
L.append('from append')
print(L)

# Count
#print('count of value 2 :',L.count(2))
#print('value is not in our list :',L.count(100))

# clear is used remove all elements from our list

#Copy
#Copy_l = L
#print('ID of L: ',id(L))
#print('ID of Copy_l: ',id(Copy_l))
#L.append(10000)
#print('ID of L: ',id(L),L)
#print('ID of Copy_l: ',id(Copy_l),Copy_l)

#copy2 = L.copy()
#print('ID of L: ',id(L),L)
#print('ID of Copy_2: ',id(copy2),copy2)

# extend is like concatination
print([1,2]+[3,4])
a = [1,2]
a.extend([3,4])
print(a)
