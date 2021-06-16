# Write a Python program to find the repeated items of a tuple.

tuple1 = (1,2,1,4,5,3,45,8,3,5) # o/p : 1,3,5

repeated = []
for i in tuple1:
    if tuple1.count(i)>1:
        if i not in repeated:
            repeated.append(i)

print(repeated)
