def check_enable(c_t,c_x,c_y,t,x,y):
    dis_t=t-c_t
    dis_x_y = c_x+c_y-x-y
    if abs(dis_x_y)>dis_t:
        #print("b")
        return False
    elif (abs(dis_x_y)-dis_t)%2==1:
        #print("a")
        return False
    else:
        #print("c")
        return True

if __name__ == "__main__":
    N = int(input())
    c_t = 0
    c_x = 0
    c_y = 0
    flag=0
    for i in range(0,N):
        t,x,y=map(int,input().split())
        if check_enable(c_t,c_x,c_y,t,x,y)==False:
            flag=1
        c_t=t
        c_x=x
        c_y=y
    print("Yes" if flag==0 else "No")
