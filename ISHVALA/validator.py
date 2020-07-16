T=int(input())
assert(T>=1 and T<=100)
for _ in range(T):
    N,M=map(int,input().split())
    X,Y,s=map(int,input().split())
    assert(X>=0 and X<=N)
    assert(Y>=0 and Y<=M)
    assert(min(N,M) >=1 and max(N,M) <=10**4)
    assert(s>=1 and s<=min(N,M))
    if X:
        x=list(map(int,input().split()))
        assert(min(x)>=1 and max(x)<=N)
        assert(x==sorted(x))
        assert(len(x)==X)
    if Y:
        y=list(map(int,input().split()))
        assert(min(y)>=1 and max(y)<=M) 
        assert(y==sorted(y))
        assert(len(y)==Y)