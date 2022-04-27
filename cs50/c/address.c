#include <stdio.h>

int main(void)
{
    char var_a = 'a';
    int int_a = 'a';
    char *p_va_char = &var_a;
    // int *p_va_int = &var_a;
    // char *p_ia_char = &int_a;
    int *p_ia_int = &int_a;

    printf("the pointer of character a as a character is %p\n", p_va_char);
    printf("the pointer of int a as an int is %p\n", p_ia_int);
    // you can not asign the different datatype of the variable, so the next two lines is not going to work
    // printf("the pointer of character a as an integer is %p", p_va_int);
    // printf("the pointer of int a as a character is %p", p_ia_char);
    
    int num = 50;
    int *p_num = &num;
    printf("the pointer of an int as an int is: %p\n", p_num);


    char *s = "HI!";
    
    printf("%p\n", &s);
    printf("%p\n", s);
    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]);
}
