# Write a program to find all the leap years in a given range
# Gregorian Calender : one year = 365.246..

def is_leap_year(year):
    if year%4==0 and (year%100!=0 or year%400==0):
        return True
    return False



start_year = int(input())
end_year = int(input())

for year in range(start_year,end_year+1):
    result = is_leap_year(year)
    if result:
        print(year)
