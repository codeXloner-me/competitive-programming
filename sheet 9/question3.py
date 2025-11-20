# Using recursion, print numbers from 1 to N. 
N = int(input())
def numbers(n):
    if n > 1:
        numbers(n - 1)
    print(n)
numbers(N)