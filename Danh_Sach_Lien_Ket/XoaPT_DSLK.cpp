#include <iostream>
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
void Xoa(Node*& head, int x)
{
	Node* p = head;
    while (head != NULL && head->info == x)
    {
        Node* p = head;
        head = head->next;
        delete p;
    }

    if (head == NULL) return;
    
    while (p->next != NULL)
    {
        if (p->next->info == x)
        {
            Node* temp = p->next;
            p->next = p->next->next;
            delete temp;
        }
        p = p->next;
    }
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
void Duyet (Node *head)
{
	Node *p = head;
	while(p != NULL)
	{
		cout << p->info <<" ";
		p=p->next;
	}
}
int main()
{
	Node *head = NULL;
	int a[1000];
	int n, x;
	cin >> n >> x;
	for(int i  =0; i< n; i++)
	{
		cin >> a[i];
		Chen_cuoi(head,a[i]);
	}
	Xoa(head,x);
	Duyet(head);
}
