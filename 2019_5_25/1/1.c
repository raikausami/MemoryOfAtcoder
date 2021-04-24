#include<stdio.h>
int main(){
    int a,b;
    int ans;
    scanf("%d %d",&a,&b);
    if(a<=5) ans=0;
    else if (6<=a && a<=12) ans = b/2;
    else{
        ans=b;
    }
    printf("%d",ans);
    return 0;
}
