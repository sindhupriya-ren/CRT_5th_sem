'''
643.Maximum Average Subarray
1343.Number of Sub-arrays of Size K and Average 
1456.
2269.
2379.
'''
from typing import List
def findMaxAverage(self, nums: List[int], k: int) -> float:
    max_sum = float("-inf")
    n = len(nums)
    for i in range(0,n-k+1):
        sub_sum = 0
        for j in range(i,k+i):
            sub_sum += nums[j]
        max_sum = max(max_sum,sub_sum)
    return max_sum/k 
nums = [1,12,-5,-6,50,3]
k = 4 
print(findMaxAverage(nums,k))







class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        win_sum = sum(nums[0:k])
        count = 0 
        if (win_sum/k) >= threshold:
            count += 1
        return count 
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4 
print(numOfSubarrays(arr,k,threshold))