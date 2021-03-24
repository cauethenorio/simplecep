import re

from .exceptions import InvalidCEPError


def clean_cep(cep: str) -> str:
    """
    ensures CEP is in the XXXXX-XXX format
    """
    try:
        match = re.match("^(\\d{5})-?(\\d{3})$", cep)
        if not match:
            raise InvalidCEPError
        return "-".join(match.groups())
    except TypeError:
        raise InvalidCEPError
