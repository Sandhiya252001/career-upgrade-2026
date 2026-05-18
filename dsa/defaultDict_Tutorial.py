from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)

# Group A
for i in range(1, n + 1):
    A = input().strip()
    d[A].append(i)

# Process B
for _ in range(m):
    B = input().strip()
    
    if B in d:
        print(" ".join(map(str, d[B])))
    else:
        print(-1)
    
  
    