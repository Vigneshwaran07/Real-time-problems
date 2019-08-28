 
#include<stdio.h>
#include<string.h>
char* Encrypt(char *str,int n)
{
  printf("%c",*(str+0));
    int i;
    for(i=0;i<n;i++)
    {
        int x=*(str+i)-'a';
       *(str+i)='z'-x;
    }
    
    return str;
}
int main()
{
    char str[20]="program";
    char *c;
   //scanf("%s",str);
    int n=strlen(str);
    c=Encrypt(&str,n);
    printf("%s",c);
    
}
