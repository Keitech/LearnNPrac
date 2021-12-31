import math
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win_start = 0
        avg = -math.inf
        temp_sum = 0
        
        for win_end in range(len(nums)):
            right_char = nums[win_end]
            temp_sum += right_char
            
            if win_end - win_start + 1 == k:
                avg = max(temp_sum/k , avg)
                temp_sum -= nums[win_start]
                win_start += 1
                
        return avg

run = Solution()

run.findMaxAverage([1,12,-5,-6,50,3], 4)