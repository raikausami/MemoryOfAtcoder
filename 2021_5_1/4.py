S = input()
T = [" "]
#D yoko
ans = []
place = 0
for i in range(0,len(S)):
    #print(i,T,S[i])
    if S[i] == T[-1]:
        del T[-1]
    elif S[i] != "R":
        T.append(S[i])
        if i ==0:
            del T[0]


for i in range(0,len(S)):
    if T[i] == "R":
        if ans[-1 
        ans.append(T[:i:-1]

print(str(''.join(T)))

