class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for string in strs:
            sort = "".join(sorted(string))
            group[sort].append(string)
        return list(group.values())
