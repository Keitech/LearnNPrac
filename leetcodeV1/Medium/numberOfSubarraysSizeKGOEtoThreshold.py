from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        win_start = 0
        count = 0
        temp_sum = 0
        
        for win_end in range(len(arr)):
            temp_sum += arr[win_end]
            
            if win_end - win_start + 1 == k:
                if temp_sum / k >= threshold:
                    count += 1
                temp_sum -= arr[win_start]
                win_start += 1
                
        return count
        

run = Solution()

run.numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4)