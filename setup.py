"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="cypherpy", # Required
    description="For cypher and decypher files and folders",  # Optional
    author="A. Trejo Gil",  # Optional
    author_email="adrian.trejo.gil@gmail.com",  # Optional
    classifiers=[ # Optional
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    package_dir={"": "src"},  # Optional
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.7, <4",
)