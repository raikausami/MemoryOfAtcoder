#include<stdio.h>
int main(){
    int h,w;
    scanf("%d %d",&h,&w);
    int tile[100][100];
    int i,j;
    int count = 0;

    for(i=0;i<h;i++){
        for(j=0;j<w;j++){
            tile[i][j]=0;
        }
    }
    for(i=0;i<h;i++){
        printf("\n");
        for(j=0;j<w;j++){
    //        printf("%d",tile[i][j]);
        }
    }


    int a,b;
    scanf("%d %d",&a,&b);
    //scanf("%d %d",&tmp1,&tmp2);
    for(i=0;i<a;i++){
        for(j=0;j<w;j++){
            tile[i][j]=1;
        }
    }
    for(i=0;i<h;i++){
        for(j=0;j<b;j++){
            tile[i][j]=1;
        }
    }
    //count
    for(i=0;i<h;i++){
        printf("\n");
        for(j=0;j<w;j++){
         //   printf("%d",tile[i][j]);
        }
    }

    for(i=0;i<h;i++){
        for(j=0;j<w;j++){
            if(tile[i][j]==0) count++;
        }
    }
    printf("%d\n",count);
    return 0;
}
