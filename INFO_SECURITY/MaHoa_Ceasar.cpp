#include<iostream>
#include<string.h>
using namespace std;

int main()
{
	int k;
	char c[1000];
	cin >> c;
	cin >> k;
	int n = strlen(c);
	for(int i = 0; i<n; i++)
	{
		int temp = c[i] - k;
		if(97 <= temp && temp <= 122)
			c[i] = char(temp);
		else if(temp < 97)
				c[i] = char(temp + 26);
	}
	cout << c;
}
