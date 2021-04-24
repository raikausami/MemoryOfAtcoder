//むずい
#include<stdio.h>
int main(){
    int A[1024][20];
    int B[20];
    char x[1024];
    int tmp_p[1024];
    scanf("%d %d %d",N,M,C);
    scanf("%s",x);
    count=0
    int a=0; //place
    for(int i=0;i<1024;i++){
        if(x[i]==" "){
            count++;
            tmp_p[a]=i;
            a++;
        }
    }

    for(int i=0;i<M;i++){
        sprintf(B[i]=

    char tmp[1024];
    for(i=0;i<N;i++){
            scanf("%s",tmp[1024]);
    }
    for(int i=0;tmp<1024;i++){
        if(tmp[i]==" "){
            count++;
        }
    }
    int correct=0;
    for(i=0;i<N;i++){
        int sum=0;
        for(j=0;j<count;j++){
            sum = sum +A[i][j]*B[j];
        }
        if(sum>0) correct++;
    }
    printf("%d",correct);
    return 0;
}
