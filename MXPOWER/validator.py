T=int(input())
assert(T>=1 and T<=100)
for t in range(T):
    N=int(input())
    assert(1<=N <=100)
    for i in range(N):
        arr=list(map(int,input().split()))
        assert(len(arr)==N)
        assert(min(arr)>=-10**9)
        assert(max(arr)<=10**9)
