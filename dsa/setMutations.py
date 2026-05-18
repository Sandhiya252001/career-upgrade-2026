N = int(input())
A = set(map(int, input().split()))

other_sets = int(input())

for _ in range(other_sets):
    First, size = input().split()
    size = int(size)

    second = set(map(int, input().split()))

    if First == "update":
        A.update(second)
    elif First == "intersection_update":
        A.intersection_update(second)
    elif First == "difference_update":
        A.difference_update(second)
    elif First == "symmetric_difference_update":
        A.symmetric_difference_update(second)

result = sum(A)
print(result)