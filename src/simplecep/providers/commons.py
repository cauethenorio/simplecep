import re
import socket
from urllib.request import urlopen, Request
from urllib.error import URLError

from typing import Optional, Dict

from simplecep.cepaddress import CEPAddress
from simplecep.exceptions import CEPProviderUnavailableError
from simplecep.utils import clean_cep


def request(
    url,
    timeout: float,
    method="GET",
    data=None,
    response_encoding="utf-8",
    headers=None,
):
    """
    Helper function to perform HTTP requests
    """
    req = Request(url, data=data, method=method, headers=headers or {})
    try:
        return urlopen(req, timeout=timeout).read().decode(response_encoding)
    except (URLError, socket.timeout, UnicodeDecodeError) as error:
        raise CEPProviderUnavailableError(error)


def build_cepaddress(provider_name: str, fields: Dict) -> CEPAddress:
    """
    Subclasses should call this function sending the fields dict
    """
    fields = extract_district(fields)

    return CEPAddress(
        cep=clean_cep(fields["cep"]),
        state=fields["state"],
        city=fields["city"],
        district=fields.get("district"),
        street=clean_street(fields.get("street")),
        provider=provider_name,
    )


def clean_street(street: Optional[str]) -> Optional[str]:
    """
    Remove numbers from street names (i.e. post office agency CEPs)
    """
    if street is not None:
        match = re.match(r"^([^,]+),?\s(\d+|s/n)$", street)
        if match is not None:
            return match.groups()[0]
        return street
    return None


def extract_district(original_fields: Dict):
    """
    Extract the Brazilian district name from the city name and send it as
    district. Example: 'Jaci Paraná (Porto Velho)' for 76840-000
    """
    fields = original_fields.copy()
    if fields.get("district") is None:
        match = re.match(r"^(.+)\s\((.+)\)$", fields["city"])
        if match:
            district, city = match.groups()
            fields["district"] = district
            fields["city"] = city
    return fields
