string="My name is sandhiya subramani"
splstr=string.split(" ")
longest=""
for splstrs in splstr:
    if len(splstrs)>len(longest):
        longest=splstrs
print(f"Longest Word is : {longest}")
