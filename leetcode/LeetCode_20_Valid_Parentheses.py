# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        maps = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in maps.values():
                stack.append(char)
            elif char in maps:
                if not stack or maps[char] != stack.pop():
                    return False
        return not stack
