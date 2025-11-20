# Problem Statement 
# Given an integer N representing the number of elements in an array, find the total number of subarrays that can be 
# generated from it. 
# Formula 
# Total Subarrays=N×(N+1)2\text{Total Subarrays} = \frac{N \times (N + 1)}{2}Total Subarrays=2N×(N+1) 
# Input Format 
# ● An integer N, the size of the array.


n = int(input())
total_subarrays = n * (n + 1) // 2
print(total_subarrays)
