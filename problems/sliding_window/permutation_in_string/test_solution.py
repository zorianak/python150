import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.checkInclusion("ab", "eidbaooo") == True

    def test_example2(self):
        assert self.solution.checkInclusion("ab", "eidboaoo") == False
