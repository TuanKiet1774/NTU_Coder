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
}
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
void Check (Node *head)
{
	if(head == NULL || head->next == NULL) 
	{
		cout << "YES";
		return;
	}
	
	Node *p = head;
	int flag = 1;
	
	
	while(p->next !=  NULL)
	{
		if(p->info > p->next->info)
		{
			flag = 0;
			break;
		}
		p=p->next;
	}
	if(flag) cout <<"YES";
	else cout <<"NO";
}
int main()
{
	int a[1000];
	Node *head = NULL;
	int n;
	cin >> n;
	for(int i = 0; i< n; i++)
	{
		cin >> a[i];
		Chen_cuoi(head,a[i]);
	}
	
	Check(head);
}
