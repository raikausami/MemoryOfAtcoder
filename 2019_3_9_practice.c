#include<stdio.h>
int main (){
    int a=0;
    while(a < 1 || 1000 < a){
        scanf("%d",&a);
    }
    int b = 0;
    int c = 0;
    while(b < 1 ||  1000 < c){
        scanf("%d %d",&b,&c);
    }
    char s[101];
    scanf("%s",s);
    printf("%d %s\n",a+b+c,s);
    return 0;
}
