#include <stdio.h>

int fibolachi(int n)
{
    if(n == 0)
        return 0;
    else if (n == 1)
        return 1;
    else
        return (fibolachi(n-1) + fibolachi(n-2));
}

int main(void)
{
    printf("%i \n", fibolachi(5));
}

