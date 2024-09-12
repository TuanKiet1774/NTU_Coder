#include<iostream>
#include<algorithm>

using namespace std;

int So_O (int n, int m, int a[])
{
	int soo = 0;
	if (m <= 1 ) 
		return 0;
	if (m <= a[0]) 
		return 1;
	int i = 0;
	
	while (m > a[i])
	{
		soo++;
		m -= (a[i] - 1);
		i++;
	}
	soo++;
	if( n<i && m - a[i-1] > 0) return -1;
	return soo;
}
int main()
{
	int n, m;
	int a[100];
	
	cin >> n >> m;
	for(int i = 0; i < n; i++)
	cin >> a[i];
	
	sort(a, a+n, greater<int>());
	
	cout << So_O(n, m, a);
}
    
