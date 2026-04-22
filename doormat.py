n, m = map(int, input().split())
c='-'
d='WELCOME'

for i in range(n):
    print((c*m).center(m,'.|.'))

# Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

#Middle Belt
for i in range(n//2):
    print((d*m*5).center(m*6))

# # Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# # Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness))
