import pytest
from solution import Codec
from solution import TreeNode


class TestCodec:
    def test_instantiation(self):
        obj = Codec()
        assert obj is not None
