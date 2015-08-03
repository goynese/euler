#include <iostream>
#include <cstdlib>
using namespace std;


long long Fibonacci(unsigned int n)
{
    if(n <= 0)
        return 0;
    if(n == 1)
        return 1;
    return Fibonacci(n-1) + Fibonacci(n - 2);
}

long long FibonacciOptimized(unsigned int n)
{
    if(n <= 0)
        return 0;
    if(n == 1)
        return 1;
    for(int i = 0; i < n; i++)
    {
        
    }
}

int main(int argc, char *argv[])
{
    cout << Fibonacci(atoi(argv[1])) << "\n";
    return 0;
}