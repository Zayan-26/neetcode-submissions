class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        running = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in running:
                return [running[diff], i]
            running[num] = i
        