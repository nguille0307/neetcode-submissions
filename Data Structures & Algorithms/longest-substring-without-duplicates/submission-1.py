class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        l = 0
        best = 0
        for r, ch in enumerate(s):
            if ch in last_index and last_index[ch] >= l:
                l = last_index[ch] + 1
            last_index[ch] = r
            best = max(best, r - l + 1)
        return best
                
