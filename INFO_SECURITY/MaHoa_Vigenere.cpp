#include <iostream>
#include <string.h>
#define max 1000
using namespace std;

void MaHoa_Vigenere(char text[], char k[], char Ma[]) 
{
	cin >> text;
	cin >> k;
	
    int textLen = strlen(text);
    int kLen = strlen(k);
    
    for (int i = 0; i < textLen; i++) 
	{
		int vt_k = i % kLen; // Vi tri ky tu cua moi ky tu trong khoa K (i luon < do dai chuoi)
        char kChar = k[vt_k]; //Moi ky tu trong khoa K
        
        char P = text[i] - 'A'; 
        char C = kChar - 'A';
        
        Ma[i] = (P + C) % 26 + 'A'; // C = (P + K) % 26
    }
    Ma[textLen] = '\0';
}

int main() 
{
    char text[max], k[max], Ma[max];
    
    MaHoa_Vigenere(text, k, Ma);
    cout << Ma;
}

//Ví dụ
//Văn bản: WEAREDISCOVEREDSAVEYOURSELF
//Khóa: DECEPTIVE
//Mã hóa: ZICVTWQNGRZGVTWAVZHCQYGLMGJ
