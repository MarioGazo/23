from src.twentythree import TwentyThree
import sys
import pytest


def test_create_correct_video():
    """ Correct run """
    sys.argv = ['test', 'create', '--type', 'video', '--title', 'a title', '--label', 'a label', '--url', 'https://www.google.com']
    tt = TwentyThree()
    assert tt.args.id is None
    assert tt.method == 'create'
    assert tt.args.type == 'video'
    assert tt.args.title == 'a title'
    assert tt.args.label == 'a label'
    assert tt.args.url == 'https://www.google.com'


def test_create_correct_photo():
    """ Correct run """
    sys.argv = ['test', 'create', '--type', 'photo', '--title', 'a title', '--label', 'a label', '--url', 'https://www.google.com']
    tt = TwentyThree()
    assert tt.method == 'create'
    assert tt.args.type == 'photo'
    assert tt.args.title == 'a title'
    assert tt.args.label == 'a label'
    assert tt.args.url == 'https://www.google.com'


def test_create_missing_type():
    """ Missing type """
    sys.argv = ['test', 'create', '--title', 'a title', '--label', 'a label', '--url', 'www.google.com']
    with pytest.raises(Exception):
        TwentyThree()


def test_create_missing_label():
    """ Missing label """
    sys.argv = ['test', 'create', '--type', 'video', '--label', 'a label', '--url', 'www.google.com']
    with pytest.raises(Exception):
        TwentyThree()


def test_create_missing_url():
    """ Missing url """
    sys.argv = ['test', 'create', '--type', 'video', '--title', 'a title', '--label', 'a label']
    with pytest.raises(Exception):
        TwentyThree()


def test_create_wrong_type():
    """ Invalid type value """
    sys.argv = ['test', 'create', '--type', 'song', '--title', 'a title', '--label', 'a label', '--url', 'www.google.com']
    with pytest.raises(Exception):
        TwentyThree()


def test_create_invalid_url():
    """ Correct run """
    sys.argv = ['test', 'create', '--type', 'video', '--title', 'a title', '--label', 'a label', '--url', 'abcd']
    with pytest.raises(Exception):
        TwentyThree()
