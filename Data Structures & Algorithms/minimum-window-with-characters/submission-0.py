from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        need = Counter(t)
        required = len(need)                     # number of distinct chars to satisfy
        have = 0                                  # number of chars in window currently satisfied

        window = {}
        left = 0
        best_len = float('inf')
        best_range = (0, 0)

        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            if ch in need and window[ch] == need[ch]:
                have += 1                         # this char's count just hit the requirement

            # While the window is VALID (covers t), try to shrink for the smallest valid
            while have == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_range = (left, right)
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1                     # we just lost coverage on this char
                left += 1

        l, r = best_range
        return s[l:r+1] if best_len != float('inf') else ""
