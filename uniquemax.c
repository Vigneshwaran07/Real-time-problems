/*i/p: n = 11
        1 1 1 2 3 4 4 4 5 6 6(i/p only  in asscending)
o/p = 5
explanation : unique max(5 isnon repeated maelement in array)*/

#include<stdio.h>
int main()
{
    int a[100],b[100],k=0,i=0,flag = 0,n,count=0;
    printf("Enter the number of elements : ");
    scanf("%d",&n);
    for(int j=0;j<n;j++)
    {
        scanf("%d",&a[j]);
    }
    while(i<n-1)
    {
      if(a[i]==a[i+1])
      {
          i = i+1;
          flag = 1;
          continue;
      }
      else if(flag==0)
      {
          b[k++]=a[i];
          flag=0;
      }
      else
      {
          flag=0;
      }
      i++;
    }
    if(a[i-1]!=a[i])
    {
        b[k++] = a[i];
    }
    if(k==0)
    {
      printf("None");
    }
    else
    {
      printf("%d",b[k-1]);
    }
}
