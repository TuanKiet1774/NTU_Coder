#include <iostream>
#include <algorithm>
#define MAX 100
using namespace std;

int main()
{
	int n, a[MAX];
	cin>>n;
	for (int i=0; i<n; i++) cin>>a[i];
	sort(a, a+n);
	int dem = 0;
	for (int i=0;i<n;i++)
		if (dem <= a[i]) dem++;	
	cout << dem;
}
    
