from random import *
seed(2804602860800033)
T=randint(80,100)
print(T)
for t in range(T):
    if t<=10:
        N=randint(1,10)
    if 11<=t<=20:
        N=randint(10,100)
    if 21<=t<=30:
        N=randint(10**2,10**3)
    if 31<=t<=40:
        N=randint(10**3,5000)
    if 41<=t<=50:
        N=randint(1,5)
    N=randint(1,8000)
    if t>=T-3:
        N=randint(1,10**5)
    print(N)
    arr=[randint(1,30) for i in range(N)]
    print(*arr)
