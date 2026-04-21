class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_nums = {}

        for num in nums:
            seen_nums[num] = seen_nums.get(num, 0) + 1

        for i, n in seen_nums.items():
            if n >= 2:
                return True
        
        return False