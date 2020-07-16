T=int(input())
assert(T>=1 and T<=100)
for _ in range(T):
    N,M=map(int,input().split())
    X,Y,s=map(int,input().split())
    assert(X>=0 and X<=N)
    assert(Y>=0 and Y<=M)
    assert(min(N,M) >=1 and max(N,M) <=10**4)
    assert(s>=1 and s<=min(N,M))
    prev_x,sum_x=0,0
    if X:
        x=list(map(int,input().split()))
        for i in range(X):
            sum_x+=(x[i]-prev_x-1)//s
            prev_x=x[i]
        assert(min(x)>=1 and max(x)<=N)
        assert(x==sorted(x))
        assert(len(x)==X)
    sum_x+=(N-prev_x)//s
    prev_y, sum_y =0,0
    if Y:
        y=list(map(int,input().split()))
        for j in range(Y):
            sum_y+=(y[j]-prev_y-1)//s
            prev_y=y[j]
        assert(min(y)>=1 and max(y)<=M) 
        assert(y==sorted(y))
        assert(len(y)==Y)
    sum_y+=(M-prev_y)//s
    print(sum_x*sum_y)