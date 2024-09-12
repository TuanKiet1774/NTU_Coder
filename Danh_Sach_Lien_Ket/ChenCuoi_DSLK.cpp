#include<iostream>
using namespace std;

struct Node 
{
	int info;
	Node *next;
};

Node *Taonut (int x)
{
	Node *n = new Node;
	n->info = x;
	n->next = NULL;
	return n;
};

Node *Chen_cuoi ( Node *&head, int x)
{
	Node *n = Taonut(x);
	if(head == NULL)
	head = n;
	else
	{
		Node *p = head;
		while(p->next != NULL)
			p = p->next;
		p->next = n;
	} 
}

void Duyet (Node * head)
{
	Node *p = head;
	while (p!=NULL)
	{
		cout << p->info <<" ";
		p=p->next;
	}
}
int main()
{
	int a[1000];
	Node *head = NULL;
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
    {
		cin >> a[i];
		Chen_cuoi(head,a[i]);
    }
    Duyet(head);
}
    
