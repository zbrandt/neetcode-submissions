class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - 97] += 1
            # num = sum([(i + 1) * n for i, n in enumerate(key)])
            num = str(key)
            if num not in groups.keys():
                groups[num] = [s]
            else:
                groups[num].append(s)
        return list(groups.values())
