#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;

//Fix this read from file function :()

vector<int> read_from_file()
{
    int c;
    vector<int> numbers;
    fstream file;
    if(file.is_open())
    {
        while(file >> c)
        {
            //Convert chars into number value. 
            numbers.push_back(c);
            cout << c << '\n';
        }
    }
    file.close();
    return numbers;
}

unsigned long long largest_series_product(std::vector<int> n)
{
    //Not the most efficent algorithm. 
    //multiple first 13 save it, keep a max, add one to iterator do 13 again.
    int j = 0;
    int sum = 1;
    unsigned long long max = 0;
    
    for(int i = 0; i <= n.size() - 13; i++)
    {
        j = i;
        sum = 1;
        while(j < i+13)
        {
            sum *= n[j];
            j++;
        }
        if(sum > max) max = sum;
    }
    return max;
}



int main () {
    //Gets all the numbers from the file. 
    vector<int> num = read_from_file();

    cout << largest_series_product(num) << '\n';
    
    return 0;
}