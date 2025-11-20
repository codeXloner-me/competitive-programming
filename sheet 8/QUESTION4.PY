# Problem Statement 
# Given an array of integers, print the sum of all possible subarrays. 
# Input Format 
# ● First line: integer N 
 
# ● Second line: N integers (array elements) 
 
# Output Format 
# ● Print the sum of each subarray, one per line. 

# code

def print_subarray_sums_simple():
    try:
        N = int(input())
    except:
        return 
    try:
        arr = list(map(int, input().split()))
    except:
        return 
    n = len(arr)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            print(current_sum)
