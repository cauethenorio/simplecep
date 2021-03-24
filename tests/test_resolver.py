import pytest
import time
from unittest import mock

from simplecep.exceptions import CouldNotResolveCepError, CEPProviderUnavailableError
from simplecep.resolver import CEPResolver


def create_mock_provider(throws=None, delay=0.0):
    """
    mock-provider factory
    """
    mock_cepaddress = mock.Mock()

    def provider(*args):
        if delay:
            time.sleep(delay)
        if throws:
            raise throws
        return mock_cepaddress

    mock_provider = mock.Mock(wraps=provider)
    return mock_provider, mock_cepaddress


@mock.patch("simplecep.resolver.clean_cep")
def test_cep_validation(clean_cep_mock):
    cep_resolver = CEPResolver([])
    cep_mock = mock.Mock()

    with pytest.raises(CouldNotResolveCepError):
        cep_resolver(cep_mock)

    clean_cep_mock.assert_called_once_with(cep_mock)


@mock.patch("simplecep.resolver.CEPResolver.resolve_cep_using_providers")
def test_cache_read(resolve_using_providers_mock):
    cepaddress_mock = mock.Mock()
    cep_resolver = CEPResolver(providers=[], cache={"12345-678": cepaddress_mock})
    assert cep_resolver("12345678") == cepaddress_mock

    resolve_using_providers_mock.assert_not_called()

    # not cached CEP should be sent to providers
    cep_resolver("00000-000")
    resolve_using_providers_mock.assert_called_once_with("00000-000")


@mock.patch("simplecep.resolver.CEPResolver.resolve_cep_using_providers")
def test_cache_write(resolve_using_providers_mock):
    cepaddress_mock = mock.Mock()
    resolve_using_providers_mock.return_value = cepaddress_mock

    cache = {}
    cep_resolver = CEPResolver(providers=[], cache=cache)
    assert cep_resolver("12345678") == cepaddress_mock

    assert "12345-678" in cache
    assert cache["12345-678"] == cepaddress_mock


def test_empty_providers():
    cep_resolver = CEPResolver(providers=[])
    with pytest.raises(CouldNotResolveCepError):
        cep_resolver("12345-678")


def test_single_working_provider():
    mock_provider, mock_cepaddress = create_mock_provider()
    cep_resolver = CEPResolver(providers=[{mock_provider}])
    assert cep_resolver("12345678") == mock_cepaddress


def test_single_failing_provider():
    mock_provider, _ = create_mock_provider(throws=CEPProviderUnavailableError)
    cep_resolver = CEPResolver(providers=[{mock_provider}])

    with pytest.raises(CouldNotResolveCepError):
        cep_resolver("12345-678")


def test_failing_and_working_providers():
    immediate_failing_mock_provider, _ = create_mock_provider(
        throws=CEPProviderUnavailableError
    )
    delayed_working_mock_provider, delayed_mock_cepaddress = create_mock_provider(
        delay=0.05
    )

    cep_resolver = CEPResolver(
        providers=[{delayed_working_mock_provider, immediate_failing_mock_provider}]
    )

    assert cep_resolver("12345678") == delayed_mock_cepaddress
    immediate_failing_mock_provider.assert_called_once()
    delayed_working_mock_provider.assert_called_once()


def test_timeout():
    timing_out_mock_provider, mock_cepaddress = create_mock_provider(delay=0.1)

    cep_resolver = CEPResolver(providers=[{timing_out_mock_provider}], timeout=0.05)

    with pytest.raises(CouldNotResolveCepError):
        cep_resolver("12345-678")

    timing_out_mock_provider.assert_called_once_with("12345-678", 0.05)
    timing_out_mock_provider.reset_mock()

    cep_resolver.timeout = 0.15
    assert cep_resolver("11111000") == mock_cepaddress
    timing_out_mock_provider.assert_called_once_with("11111-000", 0.15)


def test_use_next_group_after_group_failed():
    g1_failing_mock_provider, _ = create_mock_provider(
        throws=CEPProviderUnavailableError
    )
    g1_timing_out_mock_provider, _ = create_mock_provider(delay=0.2)

    g2_failing_mock_provider, _ = create_mock_provider(
        throws=CEPProviderUnavailableError
    )
    g2_delayed_working_mock_provider, mock_cepaddress = create_mock_provider(delay=0.05)

    cep = "11111-000"
    timeout = 0.1

    cep_resolver = CEPResolver(
        providers=[
            {g1_failing_mock_provider, g1_timing_out_mock_provider},
            {g2_failing_mock_provider, g2_delayed_working_mock_provider},
        ],
        timeout=timeout,
    )

    assert cep_resolver(cep) == mock_cepaddress
    g1_failing_mock_provider.assert_called_once_with(cep, timeout)
    g1_timing_out_mock_provider.assert_called_once_with(cep, timeout)
    g2_failing_mock_provider.assert_called_once_with(cep, timeout)
    g2_delayed_working_mock_provider.assert_called_once_with(cep, timeout)


def test_fastest_provider_use():
    """
    the result of first provider to resolve the cep should be returned
    """
    fast_mock_provider, mock_cepaddress = create_mock_provider(delay=0.05)
    slow_mock_provider, _ = create_mock_provider(delay=0.75)

    cep_resolver = CEPResolver(
        providers=[
            {slow_mock_provider, fast_mock_provider},
        ],
        timeout=0.1,
    )

    assert cep_resolver("11111000") == mock_cepaddress
    fast_mock_provider.assert_called_once_with("11111-000", 0.1)
    slow_mock_provider.assert_called_once_with("11111-000", 0.1)


def test_stop_after_success():
    """
    after resolving a cep the next provider groups should not be used
    """
    working_mock_provider, mock_cepaddress = create_mock_provider()
    next_mock_provider, _ = create_mock_provider()

    cep_resolver = CEPResolver(
        providers=[{working_mock_provider}, {next_mock_provider}],
    )

    assert cep_resolver("11111000") == mock_cepaddress
    next_mock_provider.assert_not_called()
