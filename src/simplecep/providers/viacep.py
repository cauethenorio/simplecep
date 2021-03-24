import json
import typing

from ..cepaddress import CEPAddress
from .commons import request, build_cepaddress, clean_cep, CEPProviderUnavailableError


def viacep_cep_provider(cep: str, timeout: float) -> typing.Optional[CEPAddress]:
    try:
        raw_fields = json.loads(request(get_api_url(cep), timeout=timeout))
    except json.JSONDecodeError as e:
        raise CEPProviderUnavailableError(e)

    if raw_fields.get("erro") is not True:
        return clean(raw_fields)
    return None


def get_api_url(cep: str) -> str:
    return f"https://viacep.com.br/ws/{clean_cep(cep)}/json/unicode/"


def clean(raw_fields) -> CEPAddress:
    # remove empty string fields
    fields = {k: value for k, value in raw_fields.items() if value}

    return build_cepaddress(
        "viacep",
        {
            "cep": fields["cep"],
            "state": fields["uf"],
            "city": fields["localidade"],
            "district": fields.get("bairro"),
            "street": fields.get("logradouro"),
        },
    )
