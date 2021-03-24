from io import BytesIO
from unittest import mock
import socket
from urllib.response import addinfourl
from urllib.error import HTTPError, URLError

import pytest

from simplecep.providers.commons import CEPProviderUnavailableError
from simplecep import ALL_PROVIDERS


def assert_fetcherror_is_raised_when(cep_provider, error=None, response=None):
    def fake_urlopen(*args, **kwargs):
        if error is not None:
            raise error
        return response

    with mock.patch("simplecep.providers.commons.urlopen", wraps=fake_urlopen):
        with pytest.raises(CEPProviderUnavailableError):
            cep_provider("12345689", timeout=0.1)


@pytest.mark.parametrize("cep_provider", ALL_PROVIDERS)
def test_providers_timeout_should_raise_proper_error(cep_provider):
    assert_fetcherror_is_raised_when(cep_provider, error=socket.timeout)


@pytest.mark.parametrize("cep_provider", ALL_PROVIDERS)
def test_providers_dns_error_should_raise_proper_error(cep_provider):
    dns_error = URLError(
        "gaierror(8, 'nodename nor servname provided, or not known')",
    )
    assert_fetcherror_is_raised_when(cep_provider, error=dns_error)


@pytest.mark.parametrize("cep_provider", ALL_PROVIDERS)
def test_providers_gateway_timeout_should_raise_proper_error(cep_provider):
    gateway_timeout_error = HTTPError(
        "https://fake-url.exampple.com",
        504,
        "Fake Gateway Timeout Error",
        {},
        BytesIO(b"<html>Gateway Timeout</html>"),
    )
    assert_fetcherror_is_raised_when(cep_provider, error=gateway_timeout_error)


@pytest.mark.parametrize("cep_provider", ALL_PROVIDERS)
def test_fake_success_response_invalid_encoding_raise_proper_error(cep_provider):
    fake_success_response = addinfourl(
        BytesIO(b"Unexpected content here with crazy encoding" + bytes(range(256))),
        {},
        "https://fake-url.exampple.com",
    )
    assert_fetcherror_is_raised_when(cep_provider, response=fake_success_response)


@pytest.mark.parametrize("cep_provider", ALL_PROVIDERS)
def test_fake_success_response_invalid_content_raise_proper_error(cep_provider):
    fake_success_response = addinfourl(
        BytesIO(b"Unexpected content here, not your lovely XML or JSON"),
        {},
        "https://fake-url.exampple.com",
    )
    assert_fetcherror_is_raised_when(cep_provider, response=fake_success_response)


@pytest.mark.parametrize("cep_provider", ALL_PROVIDERS)
def test_webserver_error_raise_proper_error(cep_provider):
    webserver_error = HTTPError(
        "https://fake-url.exampple.com",
        500,
        "Webserver Error",
        {},
        BytesIO(b"<html>I'm misconfigured" + bytes(range(256)) + b"</html>"),
    )
    assert_fetcherror_is_raised_when(cep_provider, error=webserver_error)
