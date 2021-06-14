# while loop

#a = 1
#while a <= 5:
#    print(a)
#   a += 1

val = 0
while val <= 10:
    if val% 2 == 0:
        print(val)
        val += 1
        continue
    elif val == 5:
        print('loop is terminated')
        break
    else: print('this is from else:  ')
    val += 1
