# Write a recursive function to find the factorial of a number. 
N = int(input())
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
result = factorial(N)
