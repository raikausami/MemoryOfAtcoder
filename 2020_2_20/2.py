N=input()
A = list(map(int, input().split()))
flag=0
for a in A:
    if a%2==0:
        if a%3!=0 and a%5!=0:
            flag=1
            

if flag==1:
    print("DENIED")
else:
    print("APPROVED")
