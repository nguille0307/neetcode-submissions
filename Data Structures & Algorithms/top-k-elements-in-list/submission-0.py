from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x for x, _ in Counter(nums).most_common(k)]
        
        