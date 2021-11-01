from setuptools import setup, find_packages

with open("README.md") as fh:
    description = fh.read

setup(
    name="AdventureGameTemplate",
    version="1.0.0",
    packages=find_packages,
    short_description = "Template for text based adventure games.",
    description=description,
    url="https://github.com/xdaiyan/AdventureGameTemplate",
    author="Daiyan Chowdhury",
    author_email="daiyanchowdhury9916@gmail.com",
    license="MIT",
    classifiers=[
        "License :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    install_requires = [
        "requests"
    ]
)