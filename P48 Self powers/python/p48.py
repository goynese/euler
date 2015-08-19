# Self powers
# Problem 48
# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

#Trivial solution in Python.
def trivial_solution(n = 1000):
	summ = 0
	for x in range(1,n + 1):
		summ += x ** x

	#grab last 10 digits.
	print summ % (10 ** 10)

trivial_solution()

#Soltion that doesn't require bigint. Works well in C++ with a long long.
#Producest last 1- digits when N is arbitrarily large.
def self_powers_mod(n = 1000):
	summ = 0
	for x in range(1, n + 1):
		summ += (x ** x) % (10 ** 10)
		summ = summ % (10 ** 10)

	print summ

self_powers_mod()