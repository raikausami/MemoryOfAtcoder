A=[]
b=[]
N=input()
A=input().split()
#print(A)

ans = []

for i in range(0,int(2*A[0]),2):
    #print()
    #print(i)
    tmp=i
    tmp2=i
    ans.append(tmp)

    for j in range(0,int(N)):
        tmp=(int(A[j])*2-tmp)
        if tmp%2:
            ans = [] 
            break

        ans.append(tmp)
        #print(tmp)

    
    if(tmp2==tmp):
        for i in range(len(ans)):
            if i == len(ans)-1:
                print()
                import sys
                sys.exit(0)

            print(ans[i], end=" ")
        
        #print("correct")

    else:
        ans = []

