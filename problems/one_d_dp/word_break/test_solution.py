import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.wordBreak("leetcode", ["leet","code"]) == True

    def test_example2(self):
        assert self.solution.wordBreak("applepenapple", ["apple","pen"]) == True
