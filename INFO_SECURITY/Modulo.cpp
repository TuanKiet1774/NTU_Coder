#include <iostream>
using namespace std;

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
    long long a, x, n;
    cin >> a >> x >> n;
    int m = modulo(a, x, n);
    if(m < 0) cout << m + n;
    else cout << m;
}

//Ví dụ
//7 16 11
//Kết quả
//4
