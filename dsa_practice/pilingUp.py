from collections import deque
T=int(input())
for _ in range(T):
    M=int(input())
    cubes=deque(map(int,input().split()))
    last = float('inf')
    possible=True
while cubes:
    if cubes[0]>=cubes[-1]:
        pick=cubes.popleft()
    else:
        pick=cubes.pop()
    if pick>last:
        possible=False
        break
    last = pick
if possible:
    print("Yes")
else:
    print("No") 
