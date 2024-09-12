#include<iostream>
#include<math.h>
using namespace std;

struct Node
{
    int info;
    Node *left;
    Node *right;
};

typedef Node *Tree;
Tree root;

Node *Tao_node(int x)
{
    Node *n = new Node;
    n->info = x;
    n->left = n->right = NULL;
    return n;
}

int Tao_NPTK(Tree &t, int x)
{
    if (t == NULL)
    {
        t = Tao_node(x);
		return 1;
    }
    if (x == t->info) return 0;
    else if (x > t->info)
        return Tao_NPTK(t->right, x);
    else
        return Tao_NPTK(t->left, x);
}

int chieucao(Tree t)
{
    if (t == NULL)
        return 0;
    if (chieucao(t->left) > chieucao(t->right))
        return chieucao(t->left) + 1;
    else
        return chieucao(t->right) + 1;
}

int check(Tree t)
{
    if (t == NULL)
        return 1;
    if (abs(chieucao(t->left) - chieucao(t->right)) > 1)
        return 0;
    else
        return check(t->left) && check(t->right);
}

int main()
{
    int a[10000];
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        Tao_NPTK(root, a[i]);
    }
    int kq = check(root);
    if (kq == 1)
        cout << "YES";
    else
        cout << "NO";
}
    
