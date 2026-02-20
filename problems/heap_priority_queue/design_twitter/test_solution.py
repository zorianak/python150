import pytest
from solution import Twitter


class TestTwitter:
    def test_instantiation(self):
        obj = Twitter()
        assert obj is not None
