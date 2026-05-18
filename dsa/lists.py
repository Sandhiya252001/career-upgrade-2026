if __name__ == '__main__':
    myList=[]
    N = int(input())
    for i in range(N):
        command = input().split()
        if command[0]=="insert":
            myList.insert(int(command[1]),int(command[2]))
        if command[0]=="append":
            myList.append(int(command[1]))
        if command[0]=="sort":
            myList.sort()
        if command[0]=="pop":
            myList.pop()
        if command[0]=="reverse":
            myList.reverse()
        if command[0]=="remove":
            myList.remove(int(command[1]))
        if command[0]=="print":
            print(myList)
