class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for k in strs:
            count = [0] * 26
            for c in k:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(k)
        return list(res.values())
     