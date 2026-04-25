N=int(input())
a=set(map(int,input().split()))
M=int(input())
b=set(map(int,input().split()))
result="\n".join(map(str,sorted(a^b)))
print(result)



