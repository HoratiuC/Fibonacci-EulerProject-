#Project Euler Problem 3
#Find the largest prime factor of a number (600851475143)

#create a function to check if a number is prime
def isprime(x):
    for n in range(2,int(x/2+1)):
        if x % n == 0:
            return False
    return True

#input your own number or use the value 600851475143
n=int(input("Enter a number:"))

#return the biggest prime factor
for i in range (2,int(n/2+1)):
    if n%i == 0:
        n = n/i
        print (n)
        if isprime(n) and n>1:
                print ("Biggest factor:",n)
                break
    

