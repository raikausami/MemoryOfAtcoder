N = input()
for i in range(0,N):
    A,B,C,D,E = list(map(int, input().split(" ")))
    if ans < H - (H-h)*D/(D-d) and  H - (H-h)*D/(D-d) >=0 :
        ans = H - (H-h)*D/(D-d)

print(ans)
ans = 0
#D yoko

for i in range(0,N):
    d,h = list(map(int, input().split(" ")))
    if ans < H - (H-h)*D/(D-d) and  H - (H-h)*D/(D-d) >=0 :
        ans = H - (H-h)*D/(D-d)

print(ans)
