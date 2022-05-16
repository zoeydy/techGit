#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    // get the input
    char input[5];
    printf("input:");
    fgets(input, 5, stdin);
    // scanf("%s", &input);

    // allocate the memory for t to store the copy of input 
    // and change t without changing input
    char *t = malloc(strlen(input)+1);
    strcpy(t,input);
    t[0] = toupper(t[0]);

    // print the t and the input
    printf("s: %s\n", input);
    printf("t: %s\n", t); 

    // free the memory
    free(t);
}
    
