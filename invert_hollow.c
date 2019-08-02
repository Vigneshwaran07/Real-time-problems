#include<stdio.h>
int main()
{

    int n,i,j,k,space;
    scanf("%d",&n);
    space = n-2;
    for(i=1;i<=n;i++)
    {
        printf("* ");
    }
    printf("\n");
    for(i=2;i<=n-1;i++)
    {
        printf("* ");
        for(j=1;j<space;j++)
        {
            printf("  ");
        }
        printf("*");
        space--;
        printf("\n");
    }
    printf("*");
}
