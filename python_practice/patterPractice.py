n,m=map(int,input().split())
for i in range(1,n,3):
    print((i*"*").center(m,'#'))
print("HELLO".center(m,'#'))
for i in range(n-2,-1,-3):
    print((i*"*").center(m,'#'))
