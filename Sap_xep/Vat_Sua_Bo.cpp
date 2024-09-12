#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    int a[n];
    for (int i = 0; i < n; ++i) 
	{
        cin >> a[i];
    }

    sort(a, a + n, greater<int>());

    int totalMilk = 0;
    for (int i = 0; i < n; ++i) 
	{
        totalMilk += max(0, a[i] - i);
    }

    cout << totalMilk;
}
    
