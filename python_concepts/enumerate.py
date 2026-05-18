#Without enumerate
fruits=['apple','orange','grapes','kiwi']
index=0
for i in fruits:
    print(index,i)
    index+=1

#Using enumeration
names=['Sandhiya','Nandhini','Mona','Shrithika','Priyanka','Nandhini','Suba','Suba','Mona']
name_map={name:[] for name in names}
for index,name in enumerate(names):
    name_map[name].append(index)
print(name_map)

