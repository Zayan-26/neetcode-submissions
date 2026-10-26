class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for num in nums:
            group[num] = 1 + group.get(num, 0)
        sort = sorted(group, key=group.get, reverse = True)
        return sort[:k]
        