# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         i=i+1
#         print(i,end="")
def print_full_name(first, last):
    # Write your code here
    return print(f"Hello {first} {last}!You just delved into python")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
