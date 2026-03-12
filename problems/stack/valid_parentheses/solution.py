from typing import List, Optional

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        pairs = {')': '(',
                 '}': '{',
                 ']': '['}
        for char in s:
            if char in pairs:
                # If its a closing character, check if there's a stack and if the last
                # char in the stack is corresponding opener
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                #if its an opening character, addit to the satck
                # for now, just assuming that its always going to be opening
                stack.append(char)
        return True if not stack else False

