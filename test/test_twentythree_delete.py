import pytest

from src.twentythree import TwentyThree
import sys


def test_delete_correct():
    """ Correct run """
    sys.argv = ['test', 'delete', '123']
    tt = TwentyThree()
    assert tt.method == 'delete'
    assert tt.args.id == 123
    assert tt.args.type is None
    assert tt.args.title is None
    assert tt.args.label is None
    assert tt.args.url is None


def test_delete_missing_id():
    """ Missing ID """
    sys.argv = ['test', 'delete']
    with pytest.raises(Exception):
        TwentyThree()
