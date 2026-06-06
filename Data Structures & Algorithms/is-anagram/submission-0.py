class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}

        for c in s:
            counter[c] = counter.get(c, 0) + 1
        
        for ch in t:
            if ch not in counter or counter[ch] == 0:
                return False
            else:
                counter[ch] -= 1
        
        return True