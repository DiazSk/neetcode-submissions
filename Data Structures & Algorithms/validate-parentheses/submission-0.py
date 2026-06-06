class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'}': '{', ')': '(', ']':'['}

        for brackets in s:
            if brackets in mapping.values():
                stack.append(brackets)
            elif brackets in mapping.keys():
                if not stack or mapping[brackets] != stack.pop():
                    return False
        
        return not stack