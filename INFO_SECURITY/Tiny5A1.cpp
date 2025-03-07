#include <iostream>
using namespace std;

char maj(char x1, char y3, char z3) 
{
    int a = x1 - '0';
    int b = y3 - '0';
    int c = z3 - '0';
    int m = (a & b) | (a & c) | (b & c);
    return m + '0'; 
}

void QuayX(string &x) 
{
    char new_x0 = ((x[2] - '0') ^ (x[4] - '0') ^ (x[5] - '0')) + '0';
    for (int i = x.length() - 1; i > 0; i--) 
    	x[i] = x[i - 1];
    x[0] = new_x0;
}

void QuayY(string &y) 
{
    char new_y0 = ((y[6] - '0') ^ (y[7] - '0')) + '0';
    for (int i = y.length() - 1; i > 0; i--) 
    	y[i] = y[i - 1];
    y[0] = new_y0;
}

void QuayZ(string &z) 
{
    char new_z0 = ((z[2] - '0') ^ (z[7] - '0') ^ (z[8] - '0')) + '0';
    for (int i = z.length() - 1; i > 0; i--) 
		z[i] = z[i - 1];
    z[0] = new_z0;
}

int main() 
{
    string x, y, z, br, bm = "";
    cin >> x >> y >> z;
    cin >> br;
    
    for (int i = 0; i < br.length(); i++) 
	{
        char m = maj(x[1], y[3], z[3]);
        
        if (x[1] == m) QuayX(x);
        if (y[3] == m) QuayY(y);
        if (z[3] == m) QuayZ(z);

        char k = ((x[5] - '0') ^ (y[7] - '0') ^ (z[8] - '0')) + '0';
        char c = ((br[i] - '0') ^ (k - '0')) + '0';
        bm += c;
    }
    
    cout << bm << endl;
}

//Ví dụ: 
//x = 100101
//y = 01001110
//z = 100110000
//Bản rõ: 111
//Kết quả: Bản mã là 011 
