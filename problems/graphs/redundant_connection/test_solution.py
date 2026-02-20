import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.findRedundantConnection([[1,2],[1,3],[2,3]]) == [2, 3]

    def test_example2(self):
        assert self.solution.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]) == [1, 4]
