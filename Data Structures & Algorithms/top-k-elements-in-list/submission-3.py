class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for num in nums:
            group[num] = group.get(num, 0) + 1
        sort = sorted(group, key=group.get, reverse = True)
        return sort[:k]

        