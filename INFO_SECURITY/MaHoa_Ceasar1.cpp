#include <iostream>
#include <string.h>
using namespace std;

int main() {
    char c[100];
    int k;
    gets(c);
    cin >> k; 

    for (int i = 0; c[i] != '\0'; i++) 
    {
        if (c[i] >= 'A' && c[i] <= 'Z')
	{  
            c[i] += k;
            if (c[i] > 'Z') c[i] -= 26;
        } 
        else if (c[i] >= 'a' && c[i] <= 'z') 
	{  
            c[i] += k;
            if (c[i] > 'z') c[i] -= 26;  
        }
    }
    cout << c;
}

