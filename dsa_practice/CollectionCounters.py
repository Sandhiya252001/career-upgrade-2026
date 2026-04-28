from collections import Counter
X=int(input())
S=input().split()
N=int(input())
price=0
count=Counter(S)
for i in range(N):
    A,B=input().split()
    if(count[A])>0:
        price+=int(B)
        count[A]-=1
print(price)

    


