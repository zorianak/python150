import pytest
from solution import TimeMap


class TestTimeMap:
    def test_instantiation(self):
        obj = TimeMap()
        assert obj is not None
