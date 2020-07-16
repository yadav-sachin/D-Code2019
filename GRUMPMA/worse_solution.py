import math
MOD=10**9+7
T=int(input())
for t in range(T):
    N,K,M=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(N):
        arr[i]%=M
    len=[0]*(K+1)
    len[0]=1
    last2=1
    for x in arr:
        last=last2
        for j in range(last2,0,-1):
            if j%M != x%M:
                continue
            len[j]=(len[j-1]+len[j])%MOD
            if j==last and last2<K: 
                last2+=1
    print(len[K]%MOD)