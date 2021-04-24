#include<stdio.h>
int main(){
    int M,N;
    int A[1024];
    int B[1024];
    double now_m=0;//money
    double low_p=0;
    if(scanf("%d %d",&N,&M)==1);
    for(int i = 0; i<N; i++){
        if(scanf("%d %d",&A[i],&B[i])==1);
    }
    low_p =10000000000000;

    for(int j=0;j<M;j++){
        for(int i = 0; i<N; i++){
            if(A[i]<low_p && B[i]>0) low_p=A[i];
        }
        for(int i = 0; i<N; i++){
            if(A[i]==low_p && B[i]>0){
 //               printf("a");
                now_m=now_m+A[i];
                B[i]--;
            }
        }
        low_p=10000000000000;;
    }
    printf("%.0lf\n",now_m);
    return 0;
}
