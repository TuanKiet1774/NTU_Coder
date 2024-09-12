#include<iostream>
using namespace std;

void xuat (int a[], int n)
{
	for(int i = 0; i<n; i++)
	{
		cout << a[i] << " ";
	}
	cout << endl;
}
void chinh (int a[], int n, int i)
{
	int k = i;
	int l = 2*i + 1;
	int r = 2*i + 2;
	if(l<n && a[l] > a[k]) k = l;
	if(r<n && a[r] > a[k]) k = r;
	if(k != i)
	{
		swap(a[i],a[k]);
		chinh(a,n,k);
	} 
}

void Build (int a[], int n)
{
	int i;
	for( i =(n/2) - 1; i>=0; i--)
	chinh(a,n,i);
}

void sx_vd (int a[], int n)
{
	Build(a,n);
	int size = n;
	while(size > 0)
	{
		xuat(a,size);
		swap(a[0],a[size -1]);
		size--;
		chinh(a,size,0);
		
	}
}

int main()
{
	int a[100];
	int n;
	cin >> n;
	for(int i = 0; i< n; i++)
	cin >> a[i];
	
	sx_vd(a,n);
}
    
