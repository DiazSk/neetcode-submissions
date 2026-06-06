from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = Counter(s)

        for ch in t:
            if ch not in s_count or s_count[ch] == 0:
                return False
            else:
                s_count[ch] -= 1
        return True