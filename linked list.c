#include<stdio.h>
#include<malloc.h>
struct node
{
    int data;
    struct node* next;
};
struct node* root = NULL;

void add(int a)
{
    struct node* temp;
    temp = (struct node*)malloc(sizeof(struct node));

    temp->data = a;
    temp->next = NULL;

    if(root == NULL)
    {
        root = temp;
    }
    else
    {
        struct node* p;
        p = root;

        while(p->next != NULL)
        {
            p = p->next;
        }
        p->next = temp;
    }
}
void addafter(int a, int value)
{
    struct node* temp, *p,*p1;
    int len = 0, i = 1;

    p1 = root;
    while(p1 != NULL)
    {
        len++;
        p1 = p1->next;
    }

    if(a>len)
    {
        printf("Invalid location\nCurrently only %d node in this list",len);
    }
    else
    {
        p = root;

        while(i<a)
        {
            p = p->next;
            i++;
        }
        temp = (struct node*)malloc(sizeof(struct node*));
        temp->data = value;
        temp->next = NULL;

        temp->next = p->next;
        p->next = temp;
    }

}



void display()
{
    struct node* temp;
    temp = root;

    if(temp == NULL)
    {
        printf("List is Empty");
    }
    else
    {
        while(temp != NULL)
        {
            printf("%d=>",temp->data);
            temp = temp->next;
        }
    }
}
int main()
{

    int choice = 0;
    while(1)
    {
    printf("1.Insert\n2.Insert at position\n3.Display\n4.Delete\n5.Exit\n");
    printf("Enter your choice :");
    scanf("%d",&choice);

    switch(choice)
    {
    case 1:
        {   int num;
            printf("Enter a number to add in list : ");
            scanf("%d",&num);
            add(num);
            break;

        }
     case 2:
        {
            int pos,val;
            printf("Enter a position and value : ");
            scanf("%d %d",&pos,&val);
            addafter(pos,val);
            break;
        }
     case 3:
        {
            display();
            break;
        }

     case 4:
        {
            int del;
            printf("Enter position :");
            scanf("%d",&del);
            delete(del);
        }
     case 5:
        {
           exit(0);
        }
    }
    printf("\n");
    }
}
