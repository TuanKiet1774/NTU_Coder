#include<iostream>
#include<stack>
using namespace std;
stack<int> s;
int main()
{
	int n, c;
	cin >> n;
	if(n==0) s.push(n);
	else
	{
		while(n>0)
		{
			s.push(n%2);
			n=n/2;
		}
	}
	while(s.size()>0)
	{
		c= s.top();
		s.pop();
		cout << c;
	}
}
    
