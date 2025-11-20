# Write a recursive function to reverse a string using recursion.
N = input()
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse(s[:-1])
result = reverse(N)
print(result)
