#include<iostream>
using namespace std;

struct Node 
{
	int info;
	Node *next;
};

Node * Tao_node (int x)
{
	Node *n = new Node;
	n->info = x;
	n->next = NULL;
	return n;
}

void Chen_cuoi (Node *&head, int x)
{
	Node *p = head;
	Node *n = Tao_node(x);
	if(head == NULL) head = n;
	else 
	{
		while(p->next != NULL)
			p = p->next;
		p->next = n;
	}
}

void chuyen (Node *&head)
{
	Node *p = head;
	while(p->next != NULL)
	p=p->next;
	Node *Q = head;
	p->next= Q;
	head = Q->next;
	Q->next = NULL;
}

void Duyet (Node *head)
{
	Node *p = head;
	while(p != NULL)
	{
		cout << p->info << " ";
		p = p->next;
	}
}

int main()
{
	Node *head = NULL;
	int a[1000];
	int n;
	cin >> n;
	for(int i = 0; i<n; i++)
	{
		cin >> a[i];
		Chen_cuoi(head,a[i]);
	}
	chuyen(head);
	Duyet(head);
}
    
