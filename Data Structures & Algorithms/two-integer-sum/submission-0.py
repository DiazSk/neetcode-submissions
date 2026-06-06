class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen_nums:
                return [seen_nums[complement], i]
            
            seen_nums[num] = i
            