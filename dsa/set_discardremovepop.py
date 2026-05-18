n = int(input())
s = set(map(int, input().split()))   

N = int(input())

for _ in range(N):
    c = input().split()

    if c[0] == "remove":
        s.remove(int(c[1]))          

    elif c[0] == "discard":
        s.discard(int(c[1]))

    elif c[0] == "pop":
        s.pop()

print(sum(s))