class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dici = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in dici:
                dici[key] = []
            dici[key].append(word)
        return list(dici.values())