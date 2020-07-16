T=int(input())
assert(T>=1 and T<=100)
rects_count=0
for t in range(T):
    N=int(input())
    assert(N>=1 and N<=10**5)
    rects_count+=N
    arr=[int(i) for i in input().split()]
    assert(len(arr)==N)
    assert(min(arr)>=1 and max(arr)<=30)
assert(rects_count<=5*10**5)