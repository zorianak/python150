import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.isPalindrome("A man, a plan, a canal: Panama") == True

    def test_example2(self):
        assert self.solution.isPalindrome("race a car") == False
