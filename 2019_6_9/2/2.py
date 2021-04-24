N=input()
a=input().split()
sum_num=0
sum_num2=0
sum_num3=10000
ans=0
b=0
c=0
for i in range(int(N)):
    sum_num=sum_num+int(a[i])
#print(sum_num)

for i in range(int(N)):
    sum_num2=sum_num2+int(a[i])
    if abs(sum_num/2-sum_num2)<sum_num3:
        sum_num3=abs(sum_num/2-sum_num2)
        ans=i


for i in range(int(N)):
    if i<=ans:
        b=b+int(a[i])
    else:
        c=c+int(a[i])
print(abs(b-c))

