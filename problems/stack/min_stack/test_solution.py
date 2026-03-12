import pytest
from solution import MinStack


class TestMinStack:
    def test_instantiation(self):
        obj = MinStack()
        assert obj is not None

    def test_top(self):
        obj = MinStack()
        obj.push(-2)
        obj.push(0)
        obj.push(-3)
        assert obj.top() == -3
