import typing

from .utils import clean_cep


class CEPAddress:
    """
    Represents a brazilian address attached to a CEP number
    """

    _data_fields: typing.List[str] = "cep street state district city".split(" ")

    _br_fields = {
        "estado": "state",
        "cidade": "city",
        "bairro": "district",
        "rua": "street",
    }

    def __init__(self, cep, state, city, district=None, street=None, provider=None):
        self.cep: str = clean_cep(cep)
        self.state: str = state
        self.city: str = city
        self.district: typing.Optional[str] = district
        self.street: typing.Optional[str] = street
        self.provider: typing.Optional[str] = provider

    def __repr__(self):
        return f"<CEPAddress {self.cep}>"

    def __eq__(self, other: typing.Any):
        if not isinstance(other, CEPAddress):
            return False

        # if all CEP fields are equal, both CEPAddresses are equal
        return all(getattr(self, f) == getattr(other, f) for f in self._data_fields)

    def to_dict(self, with_provider=False, br_names=False):
        data_fields = self._data_fields.copy()
        if with_provider:
            data_fields.append("provider")

        fields = {field: getattr(self, field) for field in data_fields}

        if br_names:
            fields = {k: fields[v] for k, v in self._br_fields.items()}

        return fields

    def __getattr__(self, item):
        try:
            field_key = self._br_fields[item]
            return getattr(self, field_key)
        except KeyError:
            raise AttributeError
