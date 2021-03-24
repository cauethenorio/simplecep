from collections.abc import MutableMapping
import concurrent.futures
from typing import Set, Sequence, Optional, Callable

from simplecep.cepaddress import CEPAddress
from simplecep.exceptions import (
    CEPProviderGroupUnavailable,
    CouldNotResolveCepError,
    CEPProviderUnavailableError,
)
from simplecep.utils import clean_cep


CEPProvider = Callable[[str, float], Optional[CEPAddress]]
ProviderGroup = Set[CEPProvider]


class CEPResolver:
    def __init__(
        self,
        providers: Sequence[ProviderGroup],
        cache: MutableMapping = None,
        timeout: float = 3,
    ):
        """
        resolvers can be a list of CEPResolver classes when all resolvers should be run in parallel
        or a list of lists of CEPResolver when some should be run before others, i.e. sequential
        """
        self.providers: Sequence[ProviderGroup] = providers
        self.timeout: float = timeout
        self.cache: MutableMapping = {} if cache is None else cache

    def __call__(self, cep: str) -> Optional[CEPAddress]:
        # make sure the CEP is valid and is in the XXXXX-XXX format
        cep = clean_cep(cep)

        try:
            return self.cache[cep]
        except KeyError:
            pass
        try:
            address = self.resolve_cep_using_providers(cep)
        except CEPProviderGroupUnavailable:
            pass
        else:
            self.cache[cep] = address
            return address

        raise CouldNotResolveCepError

    def resolve_cep_using_providers(self, cep: str) -> Optional[CEPAddress]:
        for provider_group in self.providers:
            try:
                return self.run_cep_using_provider_group(cep, provider_group)
            except CEPProviderGroupUnavailable:
                pass

        # no provider group was able to resolve the CEP
        raise CEPProviderGroupUnavailable

    def run_cep_using_provider_group(
        self, cep: str, provider_group: ProviderGroup
    ) -> CEPAddress:
        e = concurrent.futures.ThreadPoolExecutor()
        futures = [
            e.submit(cep_provider, cep, self.timeout) for cep_provider in provider_group
        ]

        try:
            for completed in concurrent.futures.as_completed(
                futures, timeout=self.timeout
            ):
                try:
                    address = completed.result()
                except CEPProviderUnavailableError:
                    pass
                else:
                    e.shutdown(wait=False)
                    return address
        except concurrent.futures.TimeoutError:
            pass

        e.shutdown(wait=False)
        raise CEPProviderGroupUnavailable
