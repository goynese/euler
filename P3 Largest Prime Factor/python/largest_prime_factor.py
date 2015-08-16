import sys
import math

def largest_prime_factor(n):
    lowfactor = 1
    for i in xrange(3, int(math.sqrt(n)), 2):
        if n%i == 0:
            if isprime(n/i):
                return n/i
            elif isprime(i):
                lowfactor = max(lowfactor,i)
    return lowfactor
    
# This is my simple prime checking program. 
def isprime(n):
    if n == 2:
        return True
    if n == 1:
        return False
    if n%2 == 0:
        return False
    for i in xrange(3, int(math.sqrt(n)) + 1, 2):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    
    # Prime found by Landry in 1867. 
    print isprime(25)
    
    # print largest_prime_factor(600851475143)
    print largest_prime_factor(int(sys.argv[1]))