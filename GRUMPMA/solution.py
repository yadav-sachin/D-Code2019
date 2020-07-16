MOD=10**9+7
T=int(input())
for t in range(T):
    N,K,M=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(N):
        arr[i]%=M
    len=[0]*(K+1)
    len[0]=1
    last=1
    for x in arr:
        y=last%M
        y=last-(y-x+M)%M
        if y==last and last<K:
            last+=1
        for j in range(y,0,-M):
            len[j]=(len[j-1]+len[j])%MOD
    print(len[K])