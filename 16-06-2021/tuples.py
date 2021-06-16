# tuple

# Creating a tuple

t = ()
t2 = tuple()
print(type(t))
print(t)
print(type(t2))

tuple_1 = (1,2,3,4,5)

print(tuple_1)

#indexing

print(tuple_1[1])
print(tuple_1[-1])
print(tuple_1[0:3])

# Methods - count(), index()

print(dir(tuple_1))

tuple2 = (1,2,3,1,2,6,7,8)

c = tuple2.count(6)
print(c)

print(tuple2.index(2))

# min, max, sum, sorted

print(min(tuple2))
print(sum(tuple2))

# Iterable
for i in tuple2:
    print(i)




