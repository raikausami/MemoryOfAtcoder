A,B,C,K = map(int,input().split())
count=0

if K<=A:
    print(K)

elif A<K and K<B:
    print(A)

else:
    print(A-(K-A-B))


