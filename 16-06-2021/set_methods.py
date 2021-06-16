# set methods

print(dir(set()))

set1 = {1,2,3,4,5}
set2 = {1,2,5,6,7}


# union(): To combine all the elements in both sets
# intersection(): The elements common to both sets

print("Union:",set1.union(set2), set1 | set2)
print("Intersection:", set1.intersection(set2), set1 & set2 )
print("Difference:",set1.difference(set2), set1-set2)
set1.difference_update(set2) #set1 = set1 - set2 #set1 = {3,4}
set2.difference_update(set1) #set2 = set2-set1
print(set1)
print(set2)

#subset : A set is called as subset when all the elements
#         in this set available in another set
# disjoint sets : There is no single common element between both sets
set1 = {1,2,3,4,5}
set2 = {1,2,5,6,7}
set3 = {1,2,3}
set4 = {4,5,6}
print("subset:",set3.issubset(set1)) # True
print("superset:",set1.issuperset(set3)) # True
print("superset(set2):",set2.issuperset(set3)) #False

print("disjoin:",set4.isdisjoint(set3))

print(id(set4))
set4.add(1)
print(set4)
print(id(set4))
set4.pop()
print(set4)
set4.pop()
print(set4)

set4.discard(4)
print(set4)

set4.remove(4)# if the element is not there in the set, then remove returns error
print(set4)



























