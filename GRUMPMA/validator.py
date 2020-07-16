import math
T=int(input())
assert(1<=T<=100)
for t in range(T):
    N,K,M=map(int,input().split())
    assert(1<=min(N,K,M))
    assert(N<=10**4)
    if not K<=N :
        print(t)
    assert(K<=N)
    if not math.ceil(K/100)<=M :
        print(t)
    assert(math.ceil(K/100)<=M)
    assert(M<=100*K)
    arr=list(map(int,input().split()))
    assert(len(arr)==N)
    assert(min(arr)>=0)
    assert(max(arr)<=10**9)