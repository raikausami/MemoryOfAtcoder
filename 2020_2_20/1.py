A = list(map(int, input().split()))
ans=0 #no
if A[0]==A[1] and A[0]!=A[2]:
    ans=1
elif A[1]==A[2] and A[0]!=A[1]:
    ans=1
elif A[0]==A[2] and A[0]!=A[1]:
    ans=1

if ans==0: print("No")
elif ans == 1: print("Yes")
