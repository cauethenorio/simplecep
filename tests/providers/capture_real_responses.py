"""
Run this file with:
> python -m tests.providers.capture_real_responses

To:
- Read all CEPs from "providers_test_data.py" file
- Request CEP addresses from all available providers
- Intercept all HTTP requests logging requests and responses
- Save responses to the "captured_responses.py" file

That file will be used by both:
- test_expected_responses.py
- test_unexpected_responses.py

To test provider functions against using saved responses,
so no real providers are contacted when tests run.
"""

import io
import os
import logging
import socket
import sys
import time
from timeit import default_timer as timer
from unittest import mock
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

from black import format_str, FileMode

from .providers_tests_data import providers_tests_data


captured_responses = []


def read_and_restore_buffer(response):
    """
    reads http.client.HTTPResponse object body and then make it readable
    again replacing the read() method with a fake one which returns a
    new unread buffer with original body content
    """

    content = response.read()
    fake_buffer = io.BytesIO(content)
    response.read = fake_buffer.read
    response.chunked = False
    response.length = len(content)
    return response, content


def get_logger():
    """
    logs whats being fetched
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    f_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    c_handler = logging.StreamHandler()
    c_handler.setFormatter(f_format)
    logger.addHandler(c_handler)
    return logger


logger = get_logger()


def patched_urlopen(req, timeout):
    """
    Captures request and response data and store
    """
    captured = {
        "request": {
            "full_url": req.full_url,
            "method": req.method,
            "headers": req.headers,
            "data": req.data,
        }
    }
    captured_error = None
    start_timer = timer()

    try:
        res = urlopen(req, timeout=timeout)
    except HTTPError as error:
        (error, content) = read_and_restore_buffer(error)
        captured_error = error
        captured["response"] = {
            "type": "error",
            "status": error.status,
            "data": content,
        }
    except (URLError, socket.timeout):
        elapsed_time = timer() - start_timer
        logger.exception(
            "Couldn't capture response (waited {elapsed_time:2.2f}s) from {method:<4} to {full_url}".format(
                elapsed_time=elapsed_time, **captured["request"]
            )
        )
        sys.exit(1)
    else:
        (res, content) = read_and_restore_buffer(res)
        captured["response"] = {"type": "success", "data": content}

    elapsed_time = timer() - start_timer

    logger.info(
        "Captured {response_type:<7} response in {elapsed_time:2.2f}s from "
        "{method:<4} to {full_url}".format(
            elapsed_time=elapsed_time,
            response_type=captured["response"]["type"],
            **captured["request"],
        )
    )

    captured_responses.append(captured)

    if captured_error:
        raise captured_error

    return res


def save_to_file(data):
    filename = "captured_responses.py"
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(dir_path, filename)

    formatted_str = format_str(repr(data), mode=FileMode())
    now_ts = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())

    content = f"""\
# This file was generated by the "{os.path.basename(__file__)}" script.
# On {now_ts}.
#
# To update it run:
# python -m tests.providers.capture_real_responses

captured_responses = {formatted_str}
"""
    with open(path, "w") as writer:
        writer.write(content)


def main():
    from simplecep.providers import ALL_PROVIDERS

    with mock.patch("simplecep.providers.commons.urlopen", wraps=patched_urlopen):
        for test_data in providers_tests_data:
            for cep_provider in ALL_PROVIDERS:
                cep_provider(test_data["input"], timeout=5)
    save_to_file(captured_responses)


if __name__ == "__main__":
    main()
