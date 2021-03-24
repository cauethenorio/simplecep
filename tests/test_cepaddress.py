from unittest import mock
import pytest

from simplecep import CEPAddress
from simplecep.exceptions import InvalidCEPError


def test_cep_validation():
    cep = CEPAddress(cep="59600050", state="RN", city="Mossoró")
    assert cep.cep == "59600-050"
    with pytest.raises(InvalidCEPError):
        CEPAddress(cep="xxxxx-xxx", state="RN", city="Mossoró")


def test_repr():
    cep = CEPAddress(cep="68925000", state="AM", city="Santana")
    assert repr(cep) == "<CEPAddress 68925-000>"


@pytest.mark.parametrize(
    "params,expected_dict",
    (
        (
            {
                "cep": "76954-000",
                "state": "RO",
                "city": "Alta Floresta d'Oeste",
            },
            {
                "cep": "76954-000",
                "state": "RO",
                "city": "Alta Floresta d'Oeste",
                "district": None,
                "street": None,
            },
        ),
        (
            {
                "cep": "69078-400",
                "state": "AM",
                "city": "Manaus",
                "district": "Japiim",
                "street": "Rua José Monteiro",
            },
            {
                "cep": "69078-400",
                "state": "AM",
                "city": "Manaus",
                "district": "Japiim",
                "street": "Rua José Monteiro",
            },
        ),
    ),
)
def test_to_dict(params, expected_dict):
    mock_provider = mock.Mock()

    partial_cep = CEPAddress(**params, provider=mock_provider)
    assert partial_cep.to_dict() == expected_dict
    assert partial_cep.to_dict(with_provider=True) == {
        **expected_dict,
        "provider": mock_provider,
    }


def test_equality():
    address_data = {"cep": "79900000", "state": "MS", "city": "Ponta Porã"}
    cepaddress1 = CEPAddress(**address_data, provider="a")
    cepaddress2 = CEPAddress(**address_data, provider="b")
    cepaddress3 = CEPAddress(**address_data, district=None, street=None)
    assert cepaddress1 == cepaddress2
    assert cepaddress1 == cepaddress3
    assert cepaddress2 == cepaddress3
    assert cepaddress1 != "79900000"
    assert cepaddress1 != 79900000

    different_address = CEPAddress(**address_data, district="Centro")
    assert cepaddress1 != different_address
