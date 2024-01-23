#include <iostream>
using namespace std;

int main()
{
    int sum = 9;
    int a[] = {1, 2, 3, 6, 7, 8};
    for (int i = 0; i < 6; i++)
    {
        for (int j = i + 1; j < 6; j++)
        {
            for(int k = j+1; k<6; k++)
            
            if (a[i] + a[j] + a[k] == sum)
            {
                cout << "Count pairs with given sum:" << sum << "is: " << a[i] << "," << a[j] <<","<<a[k] << endl;
            }
        }
    }
}