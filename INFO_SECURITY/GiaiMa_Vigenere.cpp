#include<iostream>
#include<string.h>
using namespace std;

void GiaiMa(char bm[], char k[], char br[])
{
	int n_bm = strlen(bm);
	int n_k = strlen(k);
	for(int i=0; i<n_bm; i++)
	{
		int vt_k = i % n_k;
		char kt_k = k[vt_k];
		char C = bm[i] - 'A';
		char K = kt_k - 'A';
		br[i] = (C - K + 26) % 26 + 'A';
	}
	br[n_bm] = '\0';
	cout << br;
}

int main()
{
	char bm[1000], k[1000], br[1000];
	cin >> bm >> k;
	GiaiMa(bm,k,br);
}

//vi du
//bm = PBVWETLXOZR
//k = LEG
//br = EXPLANATION
