import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.reverseBits(0b00000010100101000001111010011100) == 964176192

    def test_example2(self):
        assert self.solution.reverseBits(0b11111111111111111111111111111101) == 3221225471
