class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        check = {}
        win_start = 0
        count = 0
        
        for win_end in range(len(s)):
            left_char = s[win_end]
            if left_char not in check:
                check[left_char] = 0
            check[left_char] += 1
            
            if (win_end - win_start + 1) == 3:
                right_char = s[win_start]
                if len(check) == 3:
                    count += 1
                check[right_char] -= 1
                if check[right_char] == 0:
                    del check[right_char]
                    
                win_start += 1
                
        return count

run = Solution() 

run.countGoodSubstrings("aababcabc")