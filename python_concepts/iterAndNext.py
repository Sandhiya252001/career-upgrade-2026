arr=[1,2,3,4,5]
iteration=iter(arr)
print(iteration.__next__()) # prints 1
print(iteration.__next__()) # prints 1 2
print(next(iteration)) # prints 1 2 3


class topTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            value=self.num
            self.num+=1
            return value
        else:
            raise StopIteration
n=topTen()
for i in n:
    print(i)
