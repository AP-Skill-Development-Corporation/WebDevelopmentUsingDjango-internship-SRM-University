# calculate the sum of squares of n natural numbers

n = int(input("Enter value for n:"))
# print(sum([i**2 for i in range(1,n)]))

# calculate the sum of squares of even between n natural numbers

#result_l = []
#for i in range(1,n+1):
#    if i%2 == 0:
 #       result_l.append(i**2)
#print(sum(result_l))
#print(result_l)


#syntax for comprehension with if condition
# [expression_on_loop_variable forloop if condition(loop_varibl)]

print(sum([i**2 for i in range(1,n+1) if i%2 ==0]))
