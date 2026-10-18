class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            sort = "".join(sorted(word))
            group[sort].append(word)
        return list(group.values())