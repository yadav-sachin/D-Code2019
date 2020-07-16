req_set=[ 1<<i for i in range(30)]
T=int(input())
for _ in range(T):
    least_idx={}
    least_idx[0]=-1
    N=int(input())
    arr=list(map(int,input().split()))
    answer=0
    pre_xor=0
    for i in range(N):
        arr[i]-=1
        pre_xor^=(1<<arr[i])
        if pre_xor not in least_idx:
            least_idx[pre_xor]=i
        for j in range(30):
            req_xor=pre_xor^req_set[j]
            if req_xor in least_idx:
                answer=max(answer, i-least_idx[req_xor])
    print(answer//2)