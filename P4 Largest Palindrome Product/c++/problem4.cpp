#include <iostream>
#include <cstdlib>
#include <string>
#include <time.h>
#include <sstream>
using namespace std;

bool ispalindrome(unsigned int n)
{
    string str = to_string(n);
    if(str == string(str.rbegin(), str.rend))
        return true;
    return false
}

int largest_palindome_product(unsigned int n)
{
    int prod, max = 0;
    for(int i = n; i > 0; i--)
    {
        for(int j = n; j > 0; j--)
        {
            prod = i*j;
            if(ispalindrome(prod))
            {
                if(prod > max)
                {
                    max = prod;
                }
            }
        }
    }
    return max
}

int time_palindrome(unsigned int n)
{
    clock_t begin = clock();
    
    clock_t end = clock();
    cout << "\n" << "Time taken " << end - begin << "\n";
}


int main(int argc, char *argv[])
{
    printf("%d\n",largest_palindome_product(atoi(argv[1])));
    
    return 0;
}