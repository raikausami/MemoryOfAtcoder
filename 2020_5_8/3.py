N = int(input())
A = list(map(int,input().split()))
count=0
for i in range(1,N+1):
    #print("i",i)
    for j in range(i+1,N+1):
        #print(j)
        #print(i,j)
        if abs(i-j)==(A[i-1]+A[j-1]):
            #print(abs(i-j),abs(A[i-1]-A[j-1]))
            #print(i,j)
            count = count+1

print(count)
