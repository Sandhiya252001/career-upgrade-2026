s=input()
strin=s.split(" ")
result=[]
for i in strin:
    r=i.capitalize()
    result.append(r)
print(" ".join(result))