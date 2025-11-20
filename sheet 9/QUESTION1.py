# Write a recursive function to find the sum of the first N natural numbers. 
N = int(input())
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)
    result = sum(N)
    print(result)