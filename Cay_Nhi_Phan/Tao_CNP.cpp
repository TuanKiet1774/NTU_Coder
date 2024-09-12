#include<iostream>
using namespace std;
int a[1000];
int n;
struct Node 
{
	int info;
	Node *left ;
	Node *right;
};
typedef Node *Tree;
Tree root;

Node *Tao_nut (int x)
{
	Node *n = new Node;
	n->info = x;
	n->left = n->right =NULL;
	return n;
}

void Duyet (Tree t)
{
	if(t != NULL) 
	{
		cout << t->info <<" ";
		Duyet(t->left);
		Duyet(t->right);
	}
}

void Taocay (Tree &t, int i)
{
	if(i >= n) return;
	t = Tao_nut(a[i]);
	Taocay(t->left,2*i+1);
	Taocay(t->right,2*i+2);
}
int main()
{
	
	cin >> n;
	for(int i =0 ;i<n; i++)
	cin >> a[i];
	Taocay(root,0);
	Duyet(root);
}
    
