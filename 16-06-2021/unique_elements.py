# To get unique elements
# input : 1,2,1,3,4,53,4,5,6,9
# output : 1 2 3 4 5 6 9 53

inp = input().split(",")
for i in range(len(inp)):
    inp[i] = int(inp[i])
    
unique = sorted(set(inp))
print(unique)
