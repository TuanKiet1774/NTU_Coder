#include <iostream>
#include <string.h>
using namespace std;

#define MAX_LEN 1000

void PhaMa_DonBang(char Ma[MAX_LEN]) 
{
	cin >> Ma;
    int BangChu[26] = {0}; // chua so lan xuat hien cua cac ky tu A -> Z
    int n = strlen(Ma);
    
    for (int i = 0; i < n; i++) 
    	BangChu[Ma[i] - 'A']++;
    
    int tu1 = -1, tu2 = -1, tu3 = -1; //So lan xuat hien nhieu nhat cua 3 tu dau tien
    int vt1 = -1, vt2 = -1, vt3 = -1; //3 tu dau tien xuat hien nhieu nhat
    
    for (int i = 0; i < 26; i++) 
	{
        if (BangChu[i] > tu1) 
		{
            tu3 = tu2; 
			vt3 = vt2;
            tu2 = tu1; 
			vt2 = vt1;
            tu1 = BangChu[i]; 
			vt1 = i;
        } 
		else if (BangChu[i] > tu2) 
		{
            tu3 = tu2; 
			vt3 = vt2;
            tu2 = BangChu[i]; 
			vt2 = i;
        } 
		else if (BangChu[i] > tu3) 
		{
            tu3 = BangChu[i]; 
			vt3 = i;
        }
    }
    
    cout << char(vt1 + 'A') << " " << tu1 << endl;
    cout << char(vt2 + 'A') << " " << tu2 << endl;
    cout << char(vt3 + 'A') << " " << tu3 << endl;
    
    for (int i = 0; i < n; i++) 
	{
        if (Ma[i] == vt1 + 'A') cout << 'E';
        else if (Ma[i] == vt2 + 'A') cout << 'T';
        else if (Ma[i] == vt3 + 'A') cout << 'A';
        else cout << '-';
    }
    cout << endl;
}

int main() 
{
    char Ma[MAX_LEN];
    PhaMa_DonBang(Ma);
}

//Ví dụ
//Mã: UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZVUEPHZHMDZSHZOWSFPAPPDTSVPQUZWYMXUZUHSXEPYEPOPDZSZUFPOMBZWPPDPTGUDTMOHMQ
//kết quả:
//P 17
//Z 13
//S 10
//-T-A--------E--E-TE--A-T-AT-E-E-A-------A---T---E-T---TA-T--A-E-EE--A-E--T-----T--A--E--E-E-TAT--E---T-EE-E----------
