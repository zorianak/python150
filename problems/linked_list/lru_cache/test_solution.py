import pytest
from solution import LRUCache


class TestLRUCache:
    def test_instantiation(self):
        obj = LRUCache()
        assert obj is not None
