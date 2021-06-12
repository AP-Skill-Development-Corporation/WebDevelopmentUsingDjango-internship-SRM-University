# Write a program which takes a number from the user
# if number is divisible by 10 : o/p: divisible by 10
# else if number is divisible by 5 : o/p: divisible by 5
# else: print the number

num = int(input())
if num%10==0:
    print("Divisible by 10")
elif num%5==0:
    print("Divisible by 5")
else:
    print(num)
