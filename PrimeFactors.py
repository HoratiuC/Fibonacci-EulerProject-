def isprime(x):
    for n in range(2,int(x/2+1)):
        if x % n == 0:
            return False
    return True

n=int(input("Enter a number:"))

for i in range (2,int(n/2+1)):
    if n%i == 0:
        n = n/i
        if isprime(n):
            while n>1:
                print ("Biggest factor:",n)
        if n==1:
            break
    

