A = "bobob"
target = "bob"
count = 0
for i in range(len(A) - 2):
    if A[i:i+3] == target:
        count += 1
        
print(count) 