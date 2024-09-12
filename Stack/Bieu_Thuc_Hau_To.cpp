#include <iostream>
#include <stack>
#include <string.h>
#include <stdlib.h>
using namespace std;

int main() {
    int a, b;
    stack<int> p;
    char s[100];
    gets(s);

    int num = 0;
    for (int i = 0; i < strlen(s); i++)
	{
        if (s[i] == ' ') continue;
		else if (s[i] >= '0' && s[i] <= '9') 
		{
            while (i < strlen(s) && s[i] >= '0' && s[i] <= '9') 
			{
                num = num * 10 + (s[i] - '0');
                i++;
            }
            i--; 
			p.push(num);
            num = 0;
            }
		else 
		{
            a = p.top();
            p.pop();
            b = p.top();
            p.pop();
            int kq;
            if (s[i] == '+') kq = b + a;
            else if (s[i] == '-') kq = b - a;
            else if (s[i] == '*') kq = b * a;
            else if (s[i] == '/') kq = b / a;
            else if (s[i] == '%') kq = b % a;
            else if (s[i] == '^') 
			{
                kq = b;
                for (int j = 0; j < a - 1; j++) kq *= b;
            }
            p.push(kq);
        }
    }
    cout << p.top();
    return 0;
}
    
