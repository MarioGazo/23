from src.twentythree import TwentyThree
import sys


def test_read_correct_single():
    """ Correct run """
    sys.argv = ['test', 'read', '123']
    tt = TwentyThree()
    assert tt.method == 'read'
    assert tt.args.id == 123
    assert tt.args.type is None
    assert tt.args.title is None
    assert tt.args.label is None
    assert tt.args.url is None


def test_read_correct_all():
    """ Correct run """
    sys.argv = ['test', 'read']
    tt = TwentyThree()
    assert tt.method == 'read'
    assert tt.args.id is None
    assert tt.args.type is None
    assert tt.args.title is None
    assert tt.args.label is None
    assert tt.args.url is None


def test_row_one():
    """ Read and validate row one """
    sys.argv = ['test', 'read', '1']
    tt = TwentyThree()
    assert tt.method == 'read'
    assert tt.args.id == 1
    assert tt.args.type is None
    assert tt.args.title is None
    assert tt.args.label is None
    assert tt.args.url is None
    assert tt.response.text == '1,photo,title,label,https://google.com\n'
