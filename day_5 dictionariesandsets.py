#Word frequency counter
text = "apple banana apple orange banana apple"
words=text.split()
freq={}
for w in words:
    freq[w]=freq.get(w,0)+1
print(freq)

#Total marks
marks=dict(maths=67,science=80,english=78)
total=sum(marks.values())
print(f"Total marks : {total}")

#sets -- Removing duplicates from list
numbers=[1,2,4,5,2,5,7]
result=set(numbers)
print(result)