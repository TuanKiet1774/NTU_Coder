#include<iostream>
using namespace std;

int gcdx(int a3, int b3, int a2, int b2)
{
	if(b3 == 1) return b2;
	int q = a3 / b3;
	int r3 = a3 % b3;
	int r2 = a2 - b2 * q;
	return gcdx(b3, r3, b2, r2);
}

int main()
{
	int a, n;
	cin >> a >> n;
	
	int a3 = n, b3 = a;
	int a2 = 0, b2 = 1;
	
	int kq = gcdx(a3, b3, a2, b2);
	if(kq > 0) cout << kq;
	else
		cout << kq + n; 
}
