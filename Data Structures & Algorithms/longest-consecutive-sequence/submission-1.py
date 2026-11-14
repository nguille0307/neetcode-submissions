class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_lenght = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                lenght = 1

                while current + 1 in num_set:
                    current += 1
                    lenght +=1
                max_lenght = max(lenght, max_lenght)
        return max_lenght
                
        