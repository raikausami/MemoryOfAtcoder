import math
A,B,N = map(int,input().split())
point = 0
ans = 0
#for x in range(0,N+1):
x=N
#print(math.floor(A*x/B)-A*math.floor(x/B))
    #print(point)
    #print("p")
#    if point<math.floor(A*x/B)-A*math.floor(x/B):
point = math.floor(A*x/B)-A*math.floor(x/B)
print(point)
