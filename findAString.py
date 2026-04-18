def count_substring(string, sub_string):
    count=0
    for i in range(len(string)-len(sub_string)+1):
        #for i in range(7-3+1), last valid starting index of sub string in string is 4, we are adding 1 because python doen't take the last value in range
        #for in in range(5)

        if string[i:i+len(sub_string)]==sub_string:
            #string[0:3] , as last index not included, it will take as [0 to 2]
            count+=1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)