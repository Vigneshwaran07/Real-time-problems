 #include<stdio.h>
 int main()
 {
     int n,i,j,k;
     scanf("%d",&n);
     for(i=0;i<n+1;i++)
     {
         printf("- ");
     }
     printf("\n");
     for(i=0;i<n;i++)

     {
         printf("|");
         for(j=0;j<n-i-1;j++)
         {
             printf(" ");
         }
         for(k=0;k<i+1;k++)
         {
             printf("* ");
         }
         for(j=0;j<n-i-1;j++)
         {
             printf(" ");
         }
         printf("|");
         printf("\n");
     }
     for(i=n;i>1;i--)
     {
         printf("|");

         for(j=0;j<n-i+1;j++)
         {
             printf(" ");
         }
         for(k=0;k<i-1;k++)
         {
             printf("* ");
         }
         for(j=0;j<n-i+1;j++)
         {
             printf(" ");
         }
         printf("|");

         if(i!=1)
         {
             printf("\n");
         }


     }

     for(i=0;i<n+1;i++)
     {
         printf("- ");
     }


 }
