#include<iostream>
using namespace std;

int partition (int a[], int p, int r)
{
	int t = p;
	for(int i = p; i<=r-1; i++)
	{
		if(a[i] <= a[r])
		{
			swap(a[t],a[i]);
			t++;
		}	
	}
	swap(a[t],a[r]);
	return t;
}

int main()
{
	int a[100];
	int n;
	cin >> n;
	for(int i = 0; i<n; i++)
	{
		cin >> a[i];
	}
	
	int m = partition(a,0,n-1);
	for(int i = 0; i<n; i++)
	{
		if(i == m) cout << "[" << a[i] << "] ";
		else cout << a[i] << " " ;
	}	
}
    
