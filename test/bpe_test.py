import pytest

from nlplayground import create_vocabulary_BPE
from nlplayground import Vocabulary

def test_returns_proper_bpe_vocabulary_instance():
    assert isinstance(create_vocabulary_BPE(""), Vocabulary)

