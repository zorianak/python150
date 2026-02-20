import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    def test_example2(self):
        assert self.solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
