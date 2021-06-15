# Default arguments

def age_after_5_years(name=' ', age=0):
    result = name +' age after 5 years is '+str(age+5)
    return result

name = input("Enter name :")
age = int(input("Enter age :"))

print(age_after_5_years(name, age))
