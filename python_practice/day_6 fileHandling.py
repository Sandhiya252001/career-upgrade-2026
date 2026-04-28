f = open("python_practice/MyData.txt", "r")
print(f)
f1=open("python_practice/Demo.txt","w")
f1.write("Sandhiya Subramani")
f2=open("python_practice/Demo.txt","a")
f2.write(" Hello")
for data in f:
    f1.write(data)

f3=open("python_practice/OIP.JPG","rb")
# for i in f3:
#     print(f3)
f4=open("python_practice/MyImg.JPG","wb")
for i in f3:
    f4.write(i)