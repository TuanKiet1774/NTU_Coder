#include <iostream>
#include <cstring>
using namespace std;

int main() {
    char c[101];
    int k;

    cin.getline(c, 101); 
    cin >> k;  
    
    for (int i = 0; c[i] != '\0'; i++) 
	{
        if (c[i] >= 'A' && c[i] <= 'Z') 
			c[i] = 'A' + (c[i] - 'A' + k) % 26;
		else if (c[i] >= 'a' && c[i] <= 'z') 
			c[i] = 'a' + (c[i] - 'a' + k) % 26;
    }

    cout << c << endl;
}
    
//Ví dụ: 
//Văn bản: Doc lap - Tu do - Hanh phuc
//Khóa: 4
//Đoạn mã: Hsg pet - Xy hs - Lerl tlyg
