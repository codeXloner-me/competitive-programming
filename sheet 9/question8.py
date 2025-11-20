# Power of a number (xⁿ) 
# Problem: 
# Write a recursive function to find x raised to the power n.
X = float(input())
N = int(input())
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
result = power(X, N)
print(result)