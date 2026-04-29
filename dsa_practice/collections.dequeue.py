from collections import deque
d=deque()
N=int(input())
for i in range(N):
    a=input().split()
    if a[0]=="append":
      d.append(a[1])
    if a[0]=="appendleft":
      d.appendleft(a[1])
    if a[0]=="clear":
      d.clear()
    if a[0]=="extend":
      d.extend(a[1])
    if a[0]=="extendleft":
      d.extendleft(a[1])
    if a[0]=="pop":
      d.pop()
    if a[0]=="popleft":
      d.popleft()
    if a[0]=="extend":
      d.extend()
    if a[0]=="remove":
      d.remove()
    if a[0]=="reverse":
      d.reverse()
    if a[0]=="rotate":
      d.rotate()
print(*d)
    
      
      
      
    
