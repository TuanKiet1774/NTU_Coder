#include<iostream>
using namespace std;

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
int Tao_NPTK (Tree &t, int x)
{
	if(t == NULL)
	{
		t = Tao_node(x);
		return 1;
	}
	if(x == t->info) return 0;
	else if(x > t->info) return Tao_NPTK(t->right,x);
	else return Tao_NPTK(t->left,x);
}
int main()
{
	cin >> n;
	for(int i = 0; i < n; i++)
	{
		cin >>  a[i];
		Tao_NPTK(root,a[i]);
	}
	
	Duyet_LRN(root);
}
    
