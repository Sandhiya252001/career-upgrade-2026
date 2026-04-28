n, m = map(int, input().split())
#1st loop - range(start=1,stop=n,step=2)
#eg: here n=7
#then i values will be (1,3,5)
# Why step = 2?

# The pattern increases odd numbers of ".|.":

# 1 → .|.
# 3 → .|..|..|.
# 5 → .|..|..|..|..|.
for i in range(1, n, 2):
    print((i * '.|.').center(m, '-'))

print('WELCOME'.center(m, '-'))


#
for i in range(n-2, -1, -2):
    print((i * '.|.').center(m, '-'))