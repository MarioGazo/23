from src.twentythree import TwentyThree
import sys
import pytest


def test_twentythree_no_args():
    """ Run with no arguments results in SystemExit by ArgumentParser """
    sys.argv = ['test']
    with pytest.raises(SystemExit):
        TwentyThree()


def test_twentythree_wrong_method():
    """ Not existing method """
    sys.argv = ['test', 'test']
    with pytest.raises(Exception):
        TwentyThree()
