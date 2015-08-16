import sys
import time

# A newer simplified ispalindrome function. 
def ispalindrome(n):
    n = str(n)
    return n == n[::-1]

# def largest_palindome_product(str):
#     n = int(str)
#     for i in xrange(n,0,-1):
#         for j in xrange(n,i-1,-1):
#             print i,j, i*j
#             if ispalindrome(i*j):
#                 return i*j
def largest_palindome_product(n):
    n = int(n)
    max = 0
    cur = 0
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            cur = i*j
            if ispalindrome(cur):
                if cur > max:
                    max = cur
    return max

def time_palindrome(n):
    ti = time.time()
    for i in range(10):
        print largest_palindome_product(n)
    tf = time.time()
    
    return (tf - ti)/i

if __name__ == "__main__":
    # print largest_palindome_product(sys.argv[1])
    # Timeing for the function
    
    print time_palindrome(sys.argv[1])