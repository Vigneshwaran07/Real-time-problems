#include<stdio.h>
int main()
{

    int n,i,j,k;
    scanf("%d",&n);
    for(i=1;i<=n-1;i++)
    {
        printf("  ");
    }

    printf("*");
    printf("\n");


    for(i=2;i<=n-1;i++)
    {
        for(k=1;k<=n-i;k++)
        {
            printf("  ");
        }
        printf("* ");
        for(j=1;j<=(i*2)-3;j++)
        {
            printf("  ");
        }
        printf("* ");
        printf("\n");
    }
    for(i=0;i<(n*2)-1;i++)
    {
        printf("* ");
    }
}
