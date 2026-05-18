import re

n = int(input())
emails = [input() for _ in range(n)]

filtered_emails = list(filter(
    lambda s: re.match(r'^[\w-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$', s),
    emails
))

filtered_emails.sort()

print(filtered_emails)