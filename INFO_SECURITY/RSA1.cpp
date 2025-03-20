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

long long modulo(long long a, long long x, long long n) 
{
    if (x == 0) 
		return 1; 
    
    long long temp = modulo(a, x / 2, n);
    long long kq;
	kq = (temp * temp) % n; // temp * temp mod(n)

    if (x % 2 == 1)
        kq = (kq * a) % n;

    return kq;
}

int main()
{
	int p, q, e, M;
	
	cin >> p >> q >> e >> M;
	
	int N = p * q;
	int a3 = (q-1) * (p-1);
	int b3 = e;
	int a2 = 0, b2 = 1;
	int d = gcdx(a3, b3, a2, b2);
	

	if(d < 0) d += a3; 
	cout << e << " " << N << endl;
	cout << d << " " << N << endl;
	int C = modulo(M,d,N);
	int BM = modulo(C,e,N);
	cout << C << endl;
	cout << BM;
}
