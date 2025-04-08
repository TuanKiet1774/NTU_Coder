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
		char temp = c[i] - k;
		if('a' <= temp && temp <= 'z')
			c[i] = temp;
		else c[i] = temp + 26;
	}
	cout << c;
}

//Ví dụ: 
//Đoạn mã: wyvnyhttpun
//Khóa: 7
//Kết quả: programming
