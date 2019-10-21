import setuptools
from setuptools import setup

with open('README.md', 'rt') as readme:
    long_description = readme.read()

setup(
    name='myelftools',
    version='0.1',
    packages=setuptools.find_packages(),
    url='https://gitlab.com/efiweiss/myelftools/tree/master',
    license='MIT',
    author='efi',
    author_email='efiweiss0@gmail.com',
    description='myelftools',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
)
