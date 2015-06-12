#include<iostream>
#include<vector>
#include<math.h>
using namespace std;

long sieve_eratosthenes(long n)
{
    //Make vector 1 to n
    int i;
    std::vector<long> a(n-1);
    for(i = 2; i <= n; ++i)
    {
        a[i-2] = i;
    }
    cout << "past loop 1" << std::flush;
    //mark all non primes
    int c;
    for(int j = 0; j+1 < sqrt(n); ++j)
    {
        c = a[j];
        for(i = 2; i*c <= n; ++i)
        {
             
            long mark = i*c;
               cout << mark << std::flush;
            a[mark - 2] = -1;
        }
    }
        cout << "past loop 2" << std::flush;
    //Look through list and find primes
    std::vector <int> primes;
    for(int k = 0; k < n-1; ++k)
    {
        if(a[k] != -1)
            primes.push_back(k+2);
    }
    //Print Primes
    for(std::vector<int>::const_iterator l = primes.begin(); l != primes.end(); ++l)
        cout << *l << ' ';
     
    
}


int main(int argc, char *argv[])
{
    sieve_eratosthenes(10);
     
}