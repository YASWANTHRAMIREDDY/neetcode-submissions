
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dici = {}
        dic = {}
        for i in range(len(s)):
            if s[i] not in dici:
                dici[s[i]] = 1
            else:
                dici[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in dic:
                dic[t[j]] = 1
            else:
                dic[t[j]] += 1

        if dici == dic:
            return True
        return False
