import setuptools
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cdixsonlambdata", 
    version="1.1",
    author="C Dixson",
    author_email="crystal.dixson@gmail.com",
    description="A small example package",
    #long_description=long_description,
    #long_description_content_type="check for nulls, split a dataframe, tell me a knock knock joke",
    url="https://github.com/cdixson-ds/lambdata-12",
    packages=setuptools.find_packages()
)