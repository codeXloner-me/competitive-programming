#  1.Square root of a number
#  Given a number A. Return square root of the number if it is perfect square otherwise return-1.
#  Note: A number is a perfect square if its square root is an integer.
import math
n = int(input())
sqrt = math.isqrt(n)
if sqrt * sqrt == n:
    print(sqrt)
else:
    print(-1)
    