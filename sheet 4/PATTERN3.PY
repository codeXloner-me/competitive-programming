# Ques 3: 
# n = 5 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
n = int(input())
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()