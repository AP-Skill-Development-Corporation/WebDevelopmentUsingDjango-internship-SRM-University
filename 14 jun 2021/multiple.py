# create a table based on given input
#n = int(input('Enter a value: '))
#for i in range(1,11):
#    print(n,'*', i,'=', n*i)


n = int(input('Enter a value: '))
start = int(input('starting value: '))
end= int(input('ending value : '))
for i in range(start,end+1):
    print(n,'*', i,'=', n*i)
