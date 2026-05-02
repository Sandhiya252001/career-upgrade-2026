from collections import Counter
N=int(input())
B=[]
for _ in range(N):
    A=input()
    B.append(A)
Occ=Counter(B)
print(len(Occ))
for i in Occ.values():
    print(i,end=" ")