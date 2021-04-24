#include<stdio.h>
int main(){
    int r,d;
    int x;
    int i;
    int now;

    scanf("%d %d %d",&r,&d,&x);
    now = x;
    for(i=0;i<10;i++){
        now = now*r-d;
        printf("%d\n",now);
    }
    return 0;
}
