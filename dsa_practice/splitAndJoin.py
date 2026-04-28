def split_and_join(line):
    # write your code here
    l=line.split()
    result="-".join(l)
    print(result)
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)