class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_lenght = 0

        for nums in num_set:
            if nums - 1 not in num_set:
                current = nums
                lenght = 1

                while current + 1 in num_set:
                    current += 1
                    lenght += 1
                max_lenght = max(max_lenght, lenght)
        return max_lenght
                
        