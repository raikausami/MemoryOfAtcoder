N,M,X = map(int,input().split())
#d = map(int,input.split())
l=[list(map(int,input().split())) for i in range(N)]

for i in range(0,2**N):
    print(i)
    L = [0]*M
    flag=1
    for j in range(len(str(bin(i))),0):
        print(j)
        if str(bin(i))[j]==1:
            for k in range(0,M+1):
                L[k] += l[j][k]
                print(L)

    for n in range(1,M):
        if not L[n]>X:
            flag=0
    if flag==1:
        print(L[0])


