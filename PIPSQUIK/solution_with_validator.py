T=int(input())
assert(T>=1 and T<=100)
for _ in range(T):
    count=0
    N,H,Y1,Y2,L=map(int,input().split())
    assert(min(H,N,Y1,Y2,L)>=1)
    assert(H>1)
    assert(max(H,N,Y1,Y2,L)<=10**3)
    assert(L<=N and Y1<H)
    type=[]
    x=[]
    for i in range(N):
        t,a=map(int,input().split())
        assert(t in [1,2])
        assert(1<=a<=1000)
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