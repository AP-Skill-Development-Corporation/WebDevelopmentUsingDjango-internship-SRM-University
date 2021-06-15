# KEy word arguments
def sample_keyword(nm,age):
    result = 'after 5 years '+nm+' '+'age is '+str(age+5)
    return result

name = input('Enter Name :')
age = int(input('Enter Age :'))

print(sample_keyword(name,age))
          
