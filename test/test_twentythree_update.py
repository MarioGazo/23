from src.twentythree import TwentyThree
import pytest
import sys


def test_update_correct_single():
    """ Correct run """
    sys.argv = ['test', 'update', '123', '--title', 'a title', '--label', 'a label', '--url', 'https://www.google.com']
    tt = TwentyThree()
    assert tt.method == 'update'
    assert tt.args.id == 123
    assert tt.args.title == 'a title'
    assert tt.args.label == 'a label'
    assert tt.args.url == 'https://www.google.com'


def test_update_missing_id():
    """ Missing ID """
    sys.argv = ['test', 'update']
    with pytest.raises(Exception):
        TwentyThree()


def test_update_only_title():
    """ Update only title """
    sys.argv = ['test', 'update', '123', '--title', 'a title']
    tt = TwentyThree()
    assert tt.method == 'update'
    assert tt.args.id == 123
    assert tt.args.title == 'a title'
    assert tt.args.label is None
    assert tt.args.url is None


def test_update_only_label():
    """ Update only label """
    sys.argv = ['test', 'update', '123', '--label', 'a label']
    tt = TwentyThree()
    assert tt.method == 'update'
    assert tt.args.id == 123
    assert tt.args.title is None
    assert tt.args.label == 'a label'
    assert tt.args.url is None


def test_update_only_url():
    """ Update only url """
    sys.argv = ['test', 'update', '123', '--url', 'https://www.google.com']
    tt = TwentyThree()
    assert tt.method == 'update'
    assert tt.args.id == 123
    assert tt.args.title is None
    assert tt.args.label is None
    assert tt.args.url == 'https://www.google.com'


def test_update_row_one():
    """ Update and validate row one """
    sys.argv = ['test', 'update', '1', '--title', 'abcd']
    tt = TwentyThree()
    assert tt.method == 'update'
    assert tt.args.id == 1

    """ Read and validate row one """
    sys.argv = ['test', 'read', '1']
    tt = TwentyThree()
    assert tt.method == 'read'
    assert tt.args.id == 1
    assert tt.response.text == '1,photo,abcd,label,https://google.com\n'

    sys.argv = ['test', 'update', '1', '--title', 'title']
    tt = TwentyThree()
    assert tt.method == 'update'
    assert tt.args.id == 1

