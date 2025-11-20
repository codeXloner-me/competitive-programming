# Problem Statement 
# Given an array of integers, print all possible subarrays and their elements. 
# Input Format 
# ● First line: integer N (size of array) 
 
# ● Second line: N integers (array elements) 
 
# Output Format 
# ● Print all subarrays, one per line.

n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    for j in range(i, n):
        subarray = arr[i:j+1]
        print(' '.join(map(str, subarray)))
        