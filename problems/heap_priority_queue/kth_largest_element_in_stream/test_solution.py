import pytest
from solution import KthLargest


class TestKthLargest:
    def test_instantiation(self):
        obj = KthLargest()
        assert obj is not None
