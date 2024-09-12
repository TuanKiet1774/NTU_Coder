#include<iostream>
using namespace std;

int a[1000];
int n;

void sx_chen() 
{
    for(int i = 1; i < n; i++) 
	{
        int x = a[i];
        int j = i - 1;
        while(j >= 0 && a[j] > x) 
		{
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = x;
        for(int k = 0; k < n; k++) 
		{
            if( k== j+1 ) cout << "[" << a[k] << "] ";
            else cout << a[k] << " ";
        }
        cout << endl;
    }
}

int main() 
{
    cin >> n;
    for(int i = 0; i < n; i++)
        cin >> a[i];
    sx_chen();
    return 0;
}
    
