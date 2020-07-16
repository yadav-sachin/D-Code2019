T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    X,Y,s=map(int,input().split())
    prev_x,sum_x=0,0
    if X:
        x=list(map(int,input().split()))
        for i in range(X):
            sum_x+=(x[i]-prev_x-1)//s
            prev_x=x[i]
    sum_x+=(N-prev_x)//s
    prev_y, sum_y =0,0
    if Y:
        y=list(map(int,input().split()))
        for j in range(Y):
            sum_y+=(y[j]-prev_y-1)//s
            prev_y=y[j]
    sum_y+=(M-prev_y)//s
    print(sum_x*sum_y)