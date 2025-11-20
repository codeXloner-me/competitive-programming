# Write a recursive function to count the digits in a number. 
N = int(input())
def digit(n):
    if n == 0:
        return 0
    else:
        return 1 + digit(n // 10)
result = digit(N)