class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - 97] += 1
            key = str(chars)
            if key not in groups.keys():
                groups[key] = [s]
            else:
                groups[key].append(s)
        return list(groups.values())
