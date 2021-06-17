# Dictionary

# Create
d = {}
print(type(d))
d = {1:1,2:2,3:5}
print(d)

# Retrieve/Access

print(d[2])
print(d[3])

# Update/ Add
#{4:10}
d[4] = 10
d[2] = 4
print(d)

# {[1,2,3]:[1,4,9]}
d[(1,2,3)] = [1,4,9]
print(d)

# delete
del d[4]
print(d)




