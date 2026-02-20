import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) == 3

    def test_example2(self):
        assert self.solution.canCompleteCircuit([2,3,4], [3,4,3]) == -1
