import typing
from xml.etree import ElementTree

from simplecep.cepaddress import CEPAddress
from .commons import request, build_cepaddress, clean_cep, CEPProviderUnavailableError


def correios_sigep_cep_provider(
    cep: str, timeout: float
) -> typing.Optional[CEPAddress]:
    try:
        response = request(
            "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente",
            timeout=timeout,
            data=envelope(cep),
            method="POST",
            response_encoding="latin1",
        )
    except CEPProviderUnavailableError as e:
        original_exc = e.args[0]
        if is_cep_not_found_error(original_exc):
            return None
        raise

    fields = unenvelope(response)
    if fields is not None:
        return clean(fields)


def envelope(cep: str) -> bytearray:
    return bytearray(
        f"""
        <soapenv:Envelope
            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
            xmlns:cli="http://cliente.bean.master.sigep.bsb.correios.com.br/"
        >
           <soapenv:Header/>
           <soapenv:Body>
              <cli:consultaCEP>
                 <cep>{clean_cep(cep)}</cep>
              </cli:consultaCEP>
           </soapenv:Body>
        </soapenv:Envelope>
        """.strip(),
        "ascii",
    )


def unenvelope(response: str) -> typing.Optional[typing.Dict]:
    try:
        return_node = ElementTree.fromstring(response).find(".//return")
    except ElementTree.ParseError as e:
        raise CEPProviderUnavailableError(e)
    if return_node is not None:
        return {field.tag: field.text for field in return_node}


def clean(fields) -> CEPAddress:
    return build_cepaddress(
        "correios_sigep",
        {
            "cep": fields["cep"],
            "state": fields["uf"],
            "city": fields["cidade"],
            "district": fields.get("bairro"),
            "street": fields.get("end"),
        },
    )


def is_cep_not_found_error(exc):
    """
    Check if the 500 response is about a not found CEP.
    We don't want throw errors for that.
    """
    if getattr(exc, "code", None) != 500:
        return False

    error_response = exc.read().decode("latin1")
    try:
        message = ElementTree.fromstring(error_response).find(".//faultstring")
    except ElementTree.ParseError:
        return False
    return message is not None and message.text in (
        "CEP INVÁLIDO",
        "CEP NAO ENCONTRADO",
    )
