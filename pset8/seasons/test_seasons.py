from seasons import convert_date
import pytest

def test_valid():
    assert convert_date("1984-12-04") == "nineteen million, nine hundred and sixteen thousand, six hundred and forty minutes"


def test_invalid():
     with pytest.raises(SystemExit):
        convert_date("January 1, 1999")
