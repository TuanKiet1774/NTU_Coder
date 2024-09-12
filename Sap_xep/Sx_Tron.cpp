#include <iostream>
#define MAX 200
using namespace std;

int main()
{
	int b[MAX], c[MAX], n, m;
	cin >> n >> m;
	for (int i=0; i<n; i++) cin >> b[i];
	for (int i=0; i<m; i++) cin >> c[i];
	int i = 0, j = 0, cnt = 0;
	while (i<n && j<m)
	{
		if (b[i] <= c[j])
		{
			cout << "b" << i+1 << " ";
			++i;
		}	
		else
		{
			cout << "c" << j+1 << " ";
			++j;
		}
	}
	while (i<n) cout << "b" << ++i << " ";
	while (j<m) cout << "c" << ++j << " ";

}
    
