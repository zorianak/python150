import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_placeholder(self):
        result = self.solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        pass
