#include<iostream>
using namespace std;

int k;
int a[100];
int n;

void Xuat(int a[], int n, int vt1, int vt2)
{
    for(int i = 0; i < n; i++)
    {
        if(i == vt1 || i == vt2) 
        {
            cout << "[" << a[i] << "] ";
        }
        else 
        {
            cout << a[i] << " ";
        }
    }
    cout << endl;
}

void sx_chon(int a[], int n)
{
    for(int i = 0; i < n-1; i++)
    {
        k = i;
        for(int j = i + 1; j < n; j++)
            if(a[j] < a[k]) 
                k = j;

        if(k != i) 
        {
            swap(a[k], a[i]);
            Xuat(a, n, i, k);
        }
		else Xuat(a,n,i,k);	
    }
}

int main()
{
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    sx_chon(a, n);

    return 0;
}
    
