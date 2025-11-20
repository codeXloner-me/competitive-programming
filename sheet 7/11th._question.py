# 11. Calculator
#  WAP to make a calculator by using functions.
n = int(input())
m = int(input())
operation = input()
if operation == '+':
    result = n + m
elif operation == '-':
    result = n - m
elif operation == '*':
    result = n * m
elif operation == '/':
    result = n / m
print(result)
