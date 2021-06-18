
#n = int(input('N value:'))
# print([i**2 if i%2 == 0 else i for i in range(1,n+1)])


# write a function for prime number
# do it now
#write a function for prime number
n = int(input("Enter a number: "))  
  
if n > 1:  
   for i in range(2,n):  
       if (n % i) == 0:  
           print(n,"is not a prime number")  
           print(i,"times",n//i,"is",n)  
           break  
   else:  
       print(n,"is a prime number")  
         
else:  
   print(n,"is not a prime number")  
