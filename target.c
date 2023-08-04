#include <stdio.h>
#include <stdlib.h>

int main(){
    char * a = malloc(20);
    printf("char addr:%p\n",a);
    scanf("%s",a);
    printf("%s\n",a);
}