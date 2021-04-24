n,x=input().split()
l=input().split()
l.insert(0,0)
a=0
flag=0
for i in range(int(n)+1):
   a=a+int(l[i])
   #print(a)
   if a>int(x):
       print(i)
       flag=1
       break
if flag==0:
    print(int(n)+1)


