#include <iostream>
using namespace std;

int modulo(int a, int x, int n) 
{
    if (x == 0) return 1; 
    int temp = modulo(a, x / 2, n);
    int kq = (temp * temp) % n; // temp * temp mod(n)
    if (x % 2 == 1)
        kq = (kq * a) % n;
    return kq;
}

int main() 
{
    int a, x, n;
    cin >> a >> x >> n;
    int m = modulo(a, x, n);
    if (m < 0) cout << m + n;
    else cout << m;
}

//Ví dụ
//7 16 11
//Kết quả
//4
