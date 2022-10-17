from twttr import shorten
import pytest


def test_str():
    assert shorten("LAAAAAAMAAAAAEIO") == "LM"
    assert shorten("QsZxCv") == "QsZxCv"
    assert shorten("testing") == "tstng"
    assert shorten("this is my tweet!") == "ths s my twt!"
    assert shorten("UPPERCASE") == "PPRCS"
    assert shorten("s0meth1ng") == "s0mth1ng"

