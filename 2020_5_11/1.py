S = input()
T = input()
flag = 1
for i in range(0,len(T)):
    if not 96<ord(T[i]) and ord(T[i])<122:
        flag=0

if not len(T)-len(S)==1:
    flag=0

if not T[:-1]==S:
    flag=0
print("Yes" if flag==1 else "No")
