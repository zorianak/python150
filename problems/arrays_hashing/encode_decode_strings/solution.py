from typing import List, Optional

"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then sent over the network and is decoded back to the original list of strings.
"""

# encode with separator - num#, num is the length of the string

class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            slen = len(s)
            result += str(slen) + "#" + s
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i;
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j

        return result
