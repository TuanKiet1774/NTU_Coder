#include<iostream>
using namespace std;

int a[100];
int n;
int x;
int j;

void sx_chen(int a[], int n) 
{
    for (int i = 1; i < n; i++) 
    {
        x = a[i];
        j = i - 1;
        while (j >= 0 && a[j] > x) 
        {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = x;
        
        cout << x << " " << j + 1 << endl;
    }
}

int main() 
{
    cin >> n;

    for (int i = 0; i < n; i++)
        cin >> a[i];

    sx_chen(a, n);
}
    
