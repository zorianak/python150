import pytest
from solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example1(self):
        assert self.solution.canAttendMeetings([[0,30],[5,10],[15,20]]) == False

    def test_example2(self):
        assert self.solution.canAttendMeetings([[7,10],[2,4]]) == True
