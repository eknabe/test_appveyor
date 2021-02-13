#include <stdio.h>
#include <stdlib.h>   

int main(int argc, char* argv[])
{
    int return_value = argc > 1 ? atoi(argv[1]) : -1;
    
    printf("Hello! Returning %d.\n", return_value);
    
    return return_value;
}
