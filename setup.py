#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

setup(
    name="simplecep",
    version="0.1.0",
    description=(
        "Fetch CEP addresses consistently using Correios API, "
        "third-party APIs as fallbacks and cache the results."
    ),
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/cauethenorio/simplecep",
    author="Cauê Thenório",
    author_email="caue@thenorio.com.br",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=[],
    test_suite="tests",
    include_package_data=True,
    zip_safe=True,
    keywords=["cep", "correios", "brasil", "endereço"],
    classifiers=[
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
)
