class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = {}
        win_start = 0
        max_len = 0
        
        for i in range(len(s)):
            if s[i] in check and win_start <= check[s[i]]:
                win_start = check[s[i]] + 1
            else:
                max_len = max(i-win_start + 1, max_len)
            check[s[i]] = i
        
        return max_len
        

run = Solution()

run.lengthOfLongestSubstring("abcabcbb")