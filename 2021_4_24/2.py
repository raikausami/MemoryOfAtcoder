N = input()
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
max_a = 1
min_b = 1000
sum_num = 0
#print(N,A,B)
for i in range(0,int(N)):
    if max_a <  A[i]:
        max_a = A[i]
    if min_b > B[i]:
        min_b = B[i]

sum_num = min_b - max_a
if sum_num>=0:
    sum_num = sum_num+1
else:
    sum_num = 0
print(sum_num)
