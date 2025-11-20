# 9.Square of all numbers
#  WAPtoprint square of all numbers from x to y
x, y = map(int, input().split())
for i in range(x, y + 1):
    print(i * i)
    