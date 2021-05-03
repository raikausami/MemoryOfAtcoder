N = input()
S = list(input())
Q = input()
for s in range(0,int(Q)):
    T,a,b=(int(x) for x in input().split())
    if T == 1:
        tmp = S[int(a)-1]
        S[a-1]=S[b-1]
        S[b-1]= tmp
    elif T == 2:
        S = S[int(N):]+S[0:int(N)]
print("".join(S))
