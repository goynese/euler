import math, sys
#Sums prime less than n.

def sum_of_primes(n):
	primes = sieve_of_Eratosthenes(n)
	psum = 0
	for n in primes:
		psum += n

	print psum


#sieve of Eratosthenes

def sieve_of_Eratosthenes(limit):
	nums = list(range(limit+1))
	sqtlim = math.sqrt(limit)
	nums[1] = 0 #make 1 zero

	for n in nums[2:int(sqtlim)+1]:
		if n != 0:
			i = 2

			while n*i <= limit:
				nums[n*i] = 0
				i += 1

    #Create a list of just primes, filter out the zeros
	primes = []
	for n in nums:
		if n != 0:
			primes.append(n)

	return primes



if __name__ == '__main__':
    sum_of_primes(int(sys.argv[1]))
   
    