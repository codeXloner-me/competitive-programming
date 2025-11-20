# Check if a string is a palindrome 
# Problem: 
# Using recursion, check whether a string is a palindrome or not. 
N = input()
def palindrome(s):
    if len(s) <= 1:
        return True
    else:
        if s[0] != s[-1]:
            return False
result = palindrome(N)