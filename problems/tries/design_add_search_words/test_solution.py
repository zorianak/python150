import pytest
from solution import WordDictionary


class TestWordDictionary:
    def test_instantiation(self):
        obj = WordDictionary()
        assert obj is not None
