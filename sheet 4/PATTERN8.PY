# Ques 8: 
# n = 5 
# * * 
# * * 
# * 
# * * 
# * * 
n = int(input())
for i in range(n):
    if i == n//2:
        for j in range(1):
            print("*", end=" ")
    else:
        for j in range(2):
            print("*", end=" ")
    print()