#include <iostream>
#include <cstdlib>
#include <string>
#include <time.h>
#include <sstream>
using namespace std;

bool ispalindrome(unsigned int n)
{
    //convert integer to a string
    string str = to_string(n);
    
    for(string::const_iterator i = str.begin(), j = str.end(); i < j; i++, j--)
    {
        if(*i != *j)
            return false;
    }
    return true;
}

int main(int argc, char *argv[])
{
    clock_t begin = clock();
    if(ispalindrome(atoi(argv[1])) == true)
        cout << true;
    else
        cout << false;
    
    clock_t end = clock();
    
    cout << "\n" << "Time taken " << end - begin << "\n";
    
    
    return 0;
}