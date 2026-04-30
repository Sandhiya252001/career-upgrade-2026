from collections import Counter

s = input()

# Step 1: Count frequency
freq = Counter(s)
print(freq)
#o/p Counter({'b': 3, 'a': 2, 'c': 2, 'd': 1, 'e': 1})

# Step 2: Sort (count desc, char asc)
result = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

# Step 3: Print top 3
for ch, count in result[:3]:
    print(ch, count)