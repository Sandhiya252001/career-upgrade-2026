import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    width = 4 * size - 3

    for i in range(size):
        left = alpha[size-1:size-i-1:-1]
        right = alpha[size-i-1:size]
        row = "-".join(left + right)
        print(row.center(width, "-"))

    for i in range(size-2, -1, -1):
        left = alpha[size-1:size-i-1:-1]
        right = alpha[size-i-1:size]
        row = "-".join(left + right)
        print(row.center(width, "-"))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)