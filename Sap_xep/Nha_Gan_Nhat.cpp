#include <iostream>
#include <algorithm>
using namespace std;
long long NhaGanNhat(long long a[], long long n) {
    if (n < 2)
        return 0; 
    long long GanNhat = a[1] - a[0];
    
    for (long long i = 2; i < n; i++) {
        long long dc = a[i] - a[i - 1];
        if (dc < GanNhat) {
            GanNhat= dc;
        }
    }
    
    return GanNhat;
}
int main() {
    long long n;
    cin >> n;    
    long long* a = new long long[n];
    for (long long i = 0; i < n; i++) {
        cin >> a[i];
    }  
    sort(a, a + n); 
    long long GanNhat = NhaGanNhat(a, n);
    cout << GanNhat << endl;
    delete[] a; 
    return 0;
}
    
