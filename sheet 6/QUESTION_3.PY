def solve_is_palindrome(T, strings):
    for S in strings:
        if S == S[::-1]:
            print(1)
        else:
            print(0)