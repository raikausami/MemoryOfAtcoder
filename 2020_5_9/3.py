N,M = map(int,input().split())
if N%2 ==1:
    for i in range(1,int((N+1)/2)):
        print(i,N-i)
else:
    for i in range(1,int(N/2)):
        print(i,N+1-i)
