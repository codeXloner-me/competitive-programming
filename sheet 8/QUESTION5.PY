# Kadane's Algorithm 
# Problem Statement 
# Given an integer array nums, find the subarray with the largest sum, and return its sum. 
# Input Format 
# ● First line: integer N 
# ● Second line: N integers (array elements) 
# Output Format 
# ● Print the maximum subarray sum.

def kadane(arr):
    max = arr[0]  
    sum = arr[0] 
    for i in range(1, len(arr)):
        current_sum = max(arr[i], sum + arr[i])
        sum = max(sum,sum)
    return sum
n = int(input())
nums = list(map(int, input().split()))
result = kadane(nums)
print(result)

