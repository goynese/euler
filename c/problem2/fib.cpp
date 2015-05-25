#include <iostream>
#include <cstdlib>
using namespace std;

//Recursive Fibonacci function 

long long Fibonacci(unsigned int n)
{
    if(n <= 0)
        return 0;
    if(n == 1)
        return 1;
    return Fibonacci(n-1) + Fibonacci(n - 2);
}

int main(int argc, char *argv[])
{
    cout << Fibonacci(atoi(argv[1])) << "\n";
    return 0;
}