class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for i in strs:
            s = ''.join(sorted(i))
            m[s].append(i)
        return list(m.values())