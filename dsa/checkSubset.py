T=int(input())
result=[]
for _ in range(T):
    N=int(input())
    A=set(map(int,input().split()))
    M=int(input())
    B=set(map(int,input().split()))
    for i in A:
        if i not in B:
            r=False
            break
    else:
        r=True
    result.append(r)
for R in result:
    print(R)