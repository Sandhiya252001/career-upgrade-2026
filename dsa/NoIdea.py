n, m = map(int, input().split())

arr = list(map(int, input().split()))

A = set(map(int, input().split()))

B = set(map(int, input().split()))

count=0
for i in arr:
    if i in A:
        count += 1
    if i in B:
        count -= 1
print(count)