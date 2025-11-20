# Using recursion, print numbers from N to 1. 
N = int(input())
def reverse(n):
    if n >= 1:
        print(n)
        reverse(n - 1)
reverse(N)
