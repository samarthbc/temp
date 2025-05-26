#include <stdio.h>
#include <string.h>

int main()
{
    char buff[10];
    int pass = 0;

    printf("Enter the password: ");
    gets(buff);

    if(strcmp(buff,"12345"))
        printf("Wrong Password !!");
    else
    {
        pass = 1;
        printf("Correct Password !!\n");
    }

    if(pass)
        printf("\nRoot privileges given to user\n");
    
    return 0;
}