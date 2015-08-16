#include<iostream>

using namespace std;

long sum_of_square(int n)
{
    long sum = 0;
    for(n; n > 0; --n)
    {
        sum += n*n;
    }
    return sum;
}

long sum(int n)
{
    long sum = 0;
    for(n; n > 0; --n)
    {
        sum += n;
    }
    return sum;
}


int main(int argc, char *argv[])
{
    cout << (sum(100)*sum(100) - sum_of_square(100));
    cout << "sum" << sum(10);
}