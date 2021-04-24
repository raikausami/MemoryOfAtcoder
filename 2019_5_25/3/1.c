#include<stdio.h>
int main(){
    int n,m,i,j;
    int l[100000];
    int r[100000];
    int count=0;
    scanf("%d %d",&n,&m);
    for(i=0;i<m;i++){
        scanf("%d %d",&l[i],&r[i]);
    }
    int c;
    for(j=1;j<=n;j++){
        int flag = 0;
        for(i=0;i<m;i++){
            if(j>=l[i] && j<=r[i]){
                c=0;
            }
            else{
                flag=1;
            }
        }
        if(flag==0) count++;
    }
    printf("%d",count);
    return 0;
}



