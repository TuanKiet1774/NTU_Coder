#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    long long n;
    long long a[100000];
    cin >> n;
    for (long i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    sort(a, a + n);

    long long dem = 0;
    long long k = 1; 

    for (long i = 1; i < n; i++)
    {
        if (a[i] == a[i - 1])
        {
            k++;
        }
        else
        {
            dem += (k * (k - 1)) / 2;
            k = 1;
        }
    }


    dem += (k * (k - 1)) / 2;

    cout << dem ;
}
    
