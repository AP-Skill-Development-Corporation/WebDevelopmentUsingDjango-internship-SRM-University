# write a func to return average of cubes of all even numbers in between range
#upper limit is inclusive

def cubes_of_avg(lv,uv):
    s = 0
    c = 0
    for i in range(lv,uv+1):
        if i%2 == 0:
            s = s+i**3
            c += 1
    return s//c

lv = int(input('lower limit: '))
uv = int(input('upper limit: '))

print(cubes_of_avg(lv,uv))
