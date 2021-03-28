__author__ = """Cauê Thenório"""
__email__ = "caue@thenorio.com.br"
__version__ = "0.1.0"


from .cepaddress import CEPAddress

from .exceptions import InvalidCEPError, CouldNotResolveCepError

from .providers import (
    correios_sigep_cep_provider,
    republicavirtual_cep_provider,
    viacep_cep_provider,
    ALL_PROVIDERS,
)

from .resolver import CEPResolver


# secs to wait for each provider
DEFAULT_TIMEOUT = 2.0

DEFAULT_PROVIDERS = (
    # try to resolve the CEP using this one first
    {correios_sigep_cep_provider},
    # if the above provider fails, use third-party ones
    # in parallel using threads. the first received result will be used
    {republicavirtual_cep_provider, viacep_cep_provider},
)

# ready to use resolver with some nice defaults
resolve_cep = CEPResolver(
    providers=DEFAULT_PROVIDERS,
    timeout=DEFAULT_TIMEOUT,
)
