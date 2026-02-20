import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]

    def test_example2(self):
        assert self.solution.partitionLabels("eccbbbbdec") == [10]
