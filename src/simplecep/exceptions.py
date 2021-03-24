class BaseSimpleCEPError(Exception):
    """
    base exception for all simplecep exceptions
    """


class InvalidCEPError(BaseSimpleCEPError):
    """
    raises when a CEP with an invalid format is provided
    """


class CouldNotResolveCepError(BaseSimpleCEPError):
    """
    raises when simplecep isn't able to resolve the provided CEP
    and all resources where exhausted (cache & providers)
    """


class CEPProviderGroupUnavailable(BaseSimpleCEPError):
    """
    raises when a CEP ProviderGroup isn't able to resolve the provided CEP
    """


class CEPProviderUnavailableError(BaseSimpleCEPError):
    """
    raises when a provider isn't able to resolve the CEP
    """
