# Ques 10: 
# n = 5 
# * * * * * * * * * 
# * * * * * * * 
# * * * * * 
# * * * 
# * 
n = int(input())
for i in range(n):
    for j in range(2*(n-i)-1):
        print("*", end=" ")
    print()