import math
z=[]
ans=0
sumsum=0
N,D=(int(x) for x in input().split())
for i in range(N):
    a=input().split()
    #print(a)
    z.append(a)
#print(z)

for i in range(N):
    for j in range(i,N):
        for k in range(D):
            sumsum=sumsum+(int(z[i][k])-int(z[j][k]))**2
        if sumsum!=0 and math.sqrt(sumsum)%1==0:
            ans=ans+1
        sumsum=0

print(ans)

