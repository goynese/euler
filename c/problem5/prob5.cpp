#include <iostream>
using namespace std;

int is_div()
{
    int i = 1;
    while(1)
    {
        if(!(i%20) && !(i%19) && !(i%18) && !(i%17) && !(i%16) && !(i%15) && !(i%14) && !(i%13) && !(i%12) && !(i%11) && !(i%10) && !(i%9) && !(i%8) && !(i%7) && !(i%6))
            return i;
        i++;
    }
}

int is_div2()
{
    for(int i = 1;;i++)
        return i
}

int main(int argc, char *argv[])
{
    cout << is_div();
    return 0;
}