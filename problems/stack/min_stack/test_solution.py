import pytest
from solution import MinStack


class TestMinStack:
    def test_instantiation(self):
        obj = MinStack()
        assert obj is not None
