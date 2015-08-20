#include <iostream>
#include <cmath>
#include <stdlib.h>
using namespace std;
// Self powers
// Problem 48
// The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

// Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

//Need a power function that just cares about the last 10 digits
long long power(long long x, long long power)
{
	long long sum = x;

	for(int i = 1; i < power; i++)
	{
		sum = (x * sum) % (long long)pow(10, 10);
	}

	return sum;
}

//Self powers.
void self_powers(int n = 1000)
{
	long long sum, ten_dig = (long long)pow(10, 10);

	for(int i = 1; i <= n; i++)
	{
		sum = (sum + power(i, i)) % ten_dig;
	}

	cout << "The last ten digits are " << sum << "\n";
}

int main(int argc, char* argv[])
{
	self_powers();
	return 0;
}