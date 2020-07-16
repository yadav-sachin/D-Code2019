T=int(input())
assert(1<=T<=10)
for t in range(T):
    N,M=map(int, input().split())
    assert(min(N,M)>=1 and max(N,M)<=50)
    arr=[]
    for i in range(N):
        arr1=list(map(int, input().split()))
        assert(len(arr1)==M)
        arr=arr+arr1
    assert(min(arr)>=0 and max(arr)<=1)
    assert(len(arr)==N*M)