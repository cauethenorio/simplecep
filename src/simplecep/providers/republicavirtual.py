import json
import re
import typing

from simplecep.cepaddress import CEPAddress
from .commons import request, build_cepaddress, clean_cep, CEPProviderUnavailableError


def republicavirtual_cep_provider(
    cep: str, timeout: float
) -> typing.Optional[CEPAddress]:
    try:
        raw_fields = json.loads(
            request(
                f"http://cep.republicavirtual.com.br/web_cep.php?cep={clean_cep(cep)}&formato=json",
                timeout=timeout,
                headers={"Accept": "application/json"},
            )
        )
    except json.JSONDecodeError as e:
        raise CEPProviderUnavailableError(e)

    if int(raw_fields["resultado"]) > 0:
        return clean_and_add_cep(raw_fields, cep)
    return None


def clean_state(state: str) -> str:
    """
    Republica Virtual API returns a different state value when searching
    for a district address. (i.e. "RO  - Distrito" for 76840-000).
    So let's clean it!
    """
    return state.split(" ")[0].strip()


def clean_and_add_cep(raw_fields, cep: str) -> CEPAddress:
    # remove empty string fields
    fields = {
        k: value.strip()
        for k, value in raw_fields.items()
        if value is not None and value.strip()
    }

    if fields.get("logradouro") and fields.get("tipo_logradouro"):
        logradouro = clean_street(fields["logradouro"])
        fields["street"] = f"{fields['tipo_logradouro']} {logradouro}"

    return build_cepaddress(
        "republicavirtual",
        {
            "cep": cep,
            "state": clean_state(fields["uf"]),
            "city": fields["cidade"],
            "district": fields.get("bairro"),
            "street": fields.get("street"),
        },
    )


street_side_regex = re.compile(r" (- )?Lado (Imp|P)ar$")
street_number_regex = re.compile(r" - de \d+/\d+ a \d+/\d+")


def clean_street(street: str) -> str:
    """
    Strip "complemento" data from street field.
    Examples:
        CEP 37503-003 street value: "Geraldino Campista - de 216/217 a 869/870"
        CEP 06018-105 street value: "Analice Sturlini - Lado Impar"
    """
    street = street_side_regex.sub("", street)
    street = street_number_regex.sub("", street)
    return street
