#include<iostream>
#include<stack>
using namespace std;

stack<int>s;
int main()
{
	int n;
	cin >> n;
	while(n>1)
	{
		int i = 2;
		while (n%i != 0) i++;
		s.push(i); 
		n=n/i;
	}
	while(s.size()>0)
	{
		int c= s.top();
		s.pop();
		if(s.size() > 0) cout << c <<"*";
		else cout << c;
	}
}
    
