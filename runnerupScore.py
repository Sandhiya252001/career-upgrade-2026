if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    #input()= takes user input as a string i.e"123455"
    #input().split()= split each value of string i.e ['1','2','3','4','5','5']
    #map(int,)=map applies int to all the input values i.e[1,2,3,4,5,5]
    arr=sorted(list(set(arr)))
    #set(arr) = removes duplicates {1,2,3,4,5}
    #list(set(arr))=again converts it into list [1,2,3,4,5]
    print(arr[-2])
    