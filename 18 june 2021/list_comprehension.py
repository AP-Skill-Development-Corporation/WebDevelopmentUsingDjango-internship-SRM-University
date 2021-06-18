# list comprehension
# calcualte the sum of these 3 digits
# input= 123
# output = 6

n = input('enter a 3 digit value: ')
#result_list = []
#for digit in n:
    # print(type(digit))
 #   digit_int = int(digit)
  #  result_list.append(digit_int)

#print('sum of the 3 digits: ',sum(result_list))


# syntax
#[expression(t_var) for t_var in iterator]

print('sum of the 3 digits: ', sum([int(digit) for digit in n]))
