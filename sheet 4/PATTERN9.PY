# Ques 9: 
# n = 5 
# * 
# * * * 
# * * * * * 
# * * * * * * * 
# * * * * * * * * * 
n = int(input())
for i in range(n):
    for j in range(2*i+1):
        print("*", end=" ")
    print()