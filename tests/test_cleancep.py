import pytest

from simplecep.utils import clean_cep
from simplecep.exceptions import InvalidCEPError


@pytest.mark.parametrize(
    "input,cleaned", (("12345678", "12345-678"), ("12345-678", "12345-678"))
)
def test_valid_input(input, cleaned):
    assert clean_cep(input) == cleaned


@pytest.mark.parametrize(
    "invalid_input",
    (None, 12345678, "0000-000", "XXXXX-XXX", " 12345-678", "a99999-999", "88888-888a"),
)
def test_invalid_input(invalid_input):
    with pytest.raises(InvalidCEPError):
        assert clean_cep(invalid_input)
