def merge_the_tools(string, k):
    N = len(string)
    s = int(N/k)
    for i in range(s):
        part = string[(i*k):(k+(i*k))]
        temp = ""
        for j in part:
            if j not in temp:
                temp += j
        print(temp)
      
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)