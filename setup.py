# lambdata-coopervos/setup.py

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="repoocsov-lambdata-coopervos",
    version="3.0",
    author="Cooper Vos",
    author_email="coopervos1@gmail.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    # license="MIT",
    url="https://github.com/repoocsov/lambdata-coopervos",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)
