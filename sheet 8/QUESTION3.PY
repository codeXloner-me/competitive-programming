# Problem Statement 
# Given an integer array and two indices L and R, find the sum of elements between those indices (inclusive). 
# Input Format 
# ● First line: integer N 
 
# ● Second line: N space-separated integers 
 
# ● Third line: two integers L and R (1-based index) 
 
# Output Format 
# ● Print the sum of elements from index L to R.

n = int(input())
arr = list(map(int, input().split()))
l, r = map(int, input().split())
subarray_sum = sum(arr[l-1:r])
print(subarray_sum)