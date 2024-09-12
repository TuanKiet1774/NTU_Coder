#include<iostream>
#include<stack>
#include<string.h>
using namespace std;

stack<char> s;

int UT (char c)
{
	if(c == '^') return 5;
	else if(c == '*' || c == '/') return 4;
	else if(c == '+' || c == '-') return 3;
	return 2;
}

int main() {
    char a[20];
    cin >> a;
    int n = strlen(a);
    
    for (int i = 0; i < n; i++) 
	{
    	if(a[i] >='A' && a[i] <= 'Z') cout << a[i] << " ";
    	else if(a[i] == '(') s.push(a[i]);
		else if(a[i] == ')')
		{
			while(s.size() && s.top() != '(')
		 	{
		 		cout << s.top() << " ";
				s.pop();
			}
			 s.pop();
		}
		else if(a[i] == '+' || a[i] == '-' || a[i] == '*' || a[i] == '/' || a[i] == '^')
		{
			while(s.size() && UT(s.top()) >= UT(a[i]))
			{
				cout << s.top() <<" ";
				s.pop();
			}
			s.push(a[i]);
		}
			 
    }

    while (s.size()) 
	{
        if(s.top() != '(') cout << s.top() << " ";
        s.pop();
    }

}
    
