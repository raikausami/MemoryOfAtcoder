#include<stdio.h>

int a[100000];
int min= 1000000;
int min_num;
int n;

int find(){
    int i;
    for(i=0;i<n;i++){
        //printf("%d",a[i]);
        if(a[i]<min){
            min=a[i];
            min_num=i;
        }
    }
    return min_num;
}

int main(){
    int m,i,j;

    int o,p,w;
    double sum=0;
    scanf("%d %d",&n,&m);
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    for(i=0;i<m;i++){
        scanf("%d %d",&o,&p);
        for(j=0;j<o;j++){
            w=find();
            //printf("%d",w);
            if(a[w]<p) a[w]=p;
            min=100000000;
            min_num=-1;
        }

    }
    for(i=0;i<n;i++){
        //printf("%d\n",a[i]);
        sum=sum+a[i];
    }
    printf("%.f",sum);
    return 0;
}

