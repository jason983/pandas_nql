# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="pandas_nql",
    version="0.3.0",
    description="Pandas_nql is an open source Python library that enables natural language queries on Pandas Dataframes using the latest advances in generative AI. Inspired by OpenAI's groundbreaking language models, pandas_nql allows users to analyze data in a more intuitive way - by simply asking questions in plain English instead of writing complex code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pandas_nql.readthedocs.io/",
    author="Jason Beechum",
    author_email="jasonbeechum@yahoo.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["openai", "duckdb", "pandas"]
)