import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.validTree(5, [[0,1],[0,2],[0,3],[1,4]]) == True

    def test_example2(self):
        assert self.solution.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]) == False
