from .correios_sigep import correios_sigep_cep_provider
from .viacep import viacep_cep_provider
from .republicavirtual import republicavirtual_cep_provider

ALL_PROVIDERS = (
    correios_sigep_cep_provider,
    viacep_cep_provider,
    republicavirtual_cep_provider,
)
