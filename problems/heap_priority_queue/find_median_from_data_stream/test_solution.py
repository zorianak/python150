import pytest
from solution import MedianFinder


class TestMedianFinder:
    def test_instantiation(self):
        obj = MedianFinder()
        assert obj is not None
