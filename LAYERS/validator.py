T=int(input())
assert(1<=T<=100)
rects_count=0
for t in range(T):
    print(t)
    N,C=map(int,input().split())
    rects_count+=N
    assert(1<=N<=10**5)
    assert(1<=C<=100)
    for i in range(N):
        #print(i)
        x,y,c=map(int,input().split())
        assert(x%2==0 and x>=2 and x<=10**9)
        assert(y%2==0 and y>=2 and y<=10**9)
        assert(1<=c<=C)
print(rects_count)
assert(rects_count<=10**6)