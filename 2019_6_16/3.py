w,h,x,y=map(float,input().split())
print(type(w))
if x==w/2 and y==h/2:
    print(w*h/2)
    print(1)

elif x==w/2 and (y==0 or y == h):
    print(w*h/2)
    print(0)

elif (x==w or x==0) and y==h/2:
    print(w*h/2)
    print(0)

elif x==w/2 or y==h/2:
    print(w*h/2)
    print(0)

elif x==w or y==h:
    print(w*h/2)
    print(0)

else:
    tmpa=x*h
    tmpc=(w-x)*h
    tmpb=w*y
    tmpd=w*(h-y)

    print(max(min(tmpa,tmpc),min(tmpb,tmpd)))
    print(0)

