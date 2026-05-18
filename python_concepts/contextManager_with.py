class HandleFile:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        self.file=None
    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file
    def __exit__(self, exc_type, exc, tb):
        self.file.close()
        return False
try:
    with HandleFile('python_practice/Demo.txt','r') as file:
        content=file.read()
    raise ValueError("Error while reading the file!")
except ValueError as e:
    print(e)
print(file.closed)