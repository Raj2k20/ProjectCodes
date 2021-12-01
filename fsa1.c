#include<stdio.h>
int fibrec(int n)
{
   if (n <= 1)
      return n;
   return fibrec(n-1) + fibrec(n-2);
}
 
int main ()
{
  int n = 9;
  printf("%d", fibrec(n));
  getchar();
  return 0;
}
