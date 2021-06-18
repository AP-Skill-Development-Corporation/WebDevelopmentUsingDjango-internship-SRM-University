# function

def prime(n):
    c = 0
    for i in range(2,(n//2)+1):
        if n%i == 0:
            c += 1
    if c >= 1:
        return False
    return True

#n = int(input('enter n value:'))
#result = [i for i in range(1,n+1) if prime(i)]
#print(result)

#result = [i for i in range(1,n+1)if all(i%j !=0 for j in range(2,(i//2)+1))]
#print(result)        

n = int(input())
l = [i for i in range(2,(n)+1) if 0 not in [i%j for j in range(2,int(i/2)+1)]]
print(l)
