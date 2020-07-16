T=int(input())
assert(T>=1 and T<=100)
for _ in range(T):
    N,H,Y1,Y2,L =map(int,input().split())
    assert(min(H,N,Y1,Y2,L)>=1)
    assert(H>1)
    assert(max(H,N,Y1,Y2,L)<=10**3)
    assert(L<=N)
    assert(Y1<H)
    for i in range(N):
        type, x=map(int, input().split())
        assert(type in [1,2])
        assert(x>=1 and x<=10**3)