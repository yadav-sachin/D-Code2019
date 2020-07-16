T=int(input())
for _ in range(T):
    count=0
    N,H,Y1,Y2,L=map(int,input().split())
    type=[]
    x=[]
    for i in range(N):
        t,a=map(int,input().split())
        type.append(t)
        x.append(a)
    for j in range(N):
        if type[j]==1:
            if x[j] < H-Y1:
                L-=1
        else:
            if x[j] > Y2:
                L-=1
        if L==0:
            break
        count+=1
    print(count)