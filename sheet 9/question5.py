# Write a recursive function to find the Nth Fibonacci number.
N = int(input())
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    result = fibonacci(N)
    print(result)