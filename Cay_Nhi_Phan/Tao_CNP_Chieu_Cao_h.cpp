#include<iostream>
#include<math.h>
using namespace std;

int i;
int a[1000];
int n;
struct Node
{
	int info;
	Node *left;
	Node *right;
};
typedef Node *Tree;
Tree root;

Node *Tao_node (int x)
{
	Node *n = new Node;
	n->info = x;
	n->left = n->right = NULL;
	return n;
}
void Duyet_LRN (Tree t)
{
	if(t != NULL)
	{
		Duyet_LRN(t->left);
		Duyet_LRN(t->right);
		cout << t->info <<" ";
	}
}


int Tao_NPTK (Tree &t, int l, int r)
{
	
	if(l<=r) 
	{
		int m = (l+r)/2;
		t = Tao_node(m);
		Tao_NPTK(t->left,l,m-1);
		Tao_NPTK(t->right,m+1,r);
	}
	
}
int main()
{
	cin >> n;
	int h = pow(2,n) - 1;
	for(i = 1; i <= h; i++)
	Tao_NPTK(root,1,h);
	
	Duyet_LRN(root);
}
    
