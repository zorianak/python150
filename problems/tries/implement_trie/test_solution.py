import pytest
from solution import Trie


class TestTrie:
    def test_instantiation(self):
        obj = Trie()
        assert obj is not None
