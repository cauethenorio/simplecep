# simpleCEP

[![PyPI version](https://badge.fury.io/py/simplecep.svg)](https://pypi.org/project/simplecep/)
[![Tests Status](https://github.com/cauethenorio/simplecep/actions/workflows/tests.yml/badge.svg)](https://github.com/cauethenorio/simplecep/actions/workflows/tests.yml)
[![Coverage Status](https://coveralls.io/repos/github/cauethenorio/simplecep/badge.svg?branch=main)](https://coveralls.io/github/cauethenorio/simplecep?branch=main)
[![Compatible Python Versions](https://img.shields.io/pypi/pyversions/simplecep.svg)](https://pypi.python.org/pypi/simplecep)

Reliably resolve Brazilian CEP addresses using multiple APIs.


## Why

ECT (Correios Company) doesn't open their CEP (Brazilian Zip Codes) data, requiring
systems to fetch CEP data individually through their API or buying the full
database from their website.

Correios API (SIGEPWeb) is known for its outages, which impacts systems which
relies on resolving CEPs as addresses, as e-commerces.

This library addresses the problem using alternative CEP data APIs as fallbacks
when Correios API doesn't respond in time and caching all received results.


## How it works

The library uses the configured CEP data providers to fetch the CEP address.
Each installed provider is used until the data is successfully fetched.

It will try to get the CEP address using Correios official API and if
it fails it will use third-party API as fallbacks.

By default, it uses the following CEP APIs:
- https://www.republicavirtual.com.br
- https://viacep.com.br/

Both APIs are queried concurrently using threads, and the first received result is used.

After fetched, the retrieved address data is cached so any address-retrieval
attempt for the same CEP is resolved immediately and won't use external
providers.

The used providers, their order, and the cache mechanism can be fully
customized.

If the CEP data isn't cached and all providers fail to retrieve it,
the `CouldNotResolveCepError` exception is raised.

## Usage


### Installation

Install from PyPI

```
pip install simplecep
```


### Using the default config

The package provides a ready-to-use `resolve_cep` function which will
try to, in order:

1. Get the CEP address from the internal cache
2. Get the CEP address from the official Correios API
3. Get the CEP address, in parallel, from third-party CEP APIs:
    - https://www.republicavirtual.com.br
    - https://viacep.com.br/

It will stop on success, and the subsequent steps won't be executed.
By default, it will wait 2 seconds for each provider.

Example:

```python
>> from simplecep import resolve_cep
>> address = resolve_cep('59615350')

>> address
<CEPAddress 59615-350>

>> address.to_dict()
{
    'cep': '59615-350',
    'street': 'Rua João Simão do Nascimento',
    'district': 'Santa Delmira',
    'city': 'Mossoró',
    'state': 'RN'
}
```

The `CEPAddress` class provides the address fields in both English and
Brazilian Portuguese names:

```python
>> address
<CEPAddress 59615-350>

>> address.street
'Rua João Simão do Nascimento'

>> address.rua
'Rua João Simão do Nascimento'

>> address.city == address.cidade
True

>> address.to_dict(br_names=True)
{
    'cep': '59615-350',
    'rua': 'Rua João Simão do Nascimento',
    'bairro': 'Santa Delmira',
    'cidade': 'Mossoró',
    'estado': 'RN'
}
```


### Customization

If you need to use the providers in a different order, a custom
provider, a different cache mechanism or change the timeout, a new
resolver instance can be created using the `CEPResolver` class.

Here's how the default `resolve_cep` function is created:

```python
from simplecep import (
    CEPResolver,
    correios_sigep_cep_provider,
    republicavirtual_cep_provider,
    viacep_cep_provider
)

resolve_cep = CEPResolver(
    providers=[
        # this resolver will first try to use the Correios API,
        {correios_sigep_cep_provider},
        # if it fails it will fall back to the RepublicaVirtual and ViaCEP APIs
        # it will spawn two threads and will query both APIs at the same time
        # the result from the first one to reply will be used
        {republicavirtual_cep_provider, viacep_cep_provider},
    ],
    # by default it will wait for each provider for 1 second
    timeout=2,
    # all fetched CEP data will be stored in the
    # cache object which is a dict but can be any dict-like object
    cache={}
)
```


#### Providers Order

The `providers` argument should be a list of sets specifying which
providers should be used, and the order they should be called.

When called, the resolver iterate over the list calling all providers in
each set concurrently using threads.

When the CEP is successfully resolved by a provider, the iteration stops
and the following provider sets are not executed.

Here's an example of `providers` param which will query all APIs
concurrently and use the first received result:

```python
brute_resolver = CEPResolver(
    providers=[
        {
            correios_sigep_cep_provider,
            republicavirtual_cep_provider,
            viacep_cep_provider
        }
    ]
)
```


#### Custom providers

Custom providers can be used to fetch CEP data from different sources.

The provider should be a callable which accepts `cep` and `timeout` as
parameters and returns a `CEPAddress` object when a CEP is found and
`None` when the CEP doesn't exist:

```python
def my_custom_provder(cep: str, timeout: float) -> Optional[CEPAdress]:
    pass # my implementation here
```

Custom providers should raise the `CEPProviderUnavailableError` error
when they fail to contact their data source or if the data source
doesn't reply before the specified `timeout` interval.

Provider-auxiliary functions are available in the
`simplecep.providers.commons` module.


#### Custom cache

By default, a dict object is used as cache, it's good enough to avoid
querying for the same CEP twice in the same process, but it has limitations as:
- Different processes can't share the cache (i.e. web-workers)
- The cache is destroyed when the process is killed

So a custom object can be used as cache, it needs to be a dict-like object
(i.e. implements `__getitem__` and `__setitem__`).

A good example is the `redis-dict` project which creates a dict-like object
which stores the values on Redis: https://pypi.org/project/redis-dict/


# Testing

Tests are found in the ```tests``` folder. Install the requirements in
the `dev_requirements.txt` file and run `make test` to run the tests.

# License

See [License](LICENSE).
