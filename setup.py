import io
import os
from pathlib import Path

from setuptools import find_packages, setup


# Metadata of package
NAME = 'src'
DESCRIPTION = 'Olist sentment analysis'
AUTHOR = 'Victor Oliveira'
REQUIRES_PYTHON = '>=3.10.7'

pwd = os.path.abspath(os.path.dirname(__file__))


# Load the package's __version__.py module as a dictionary.
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
about = {}
with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=('tests',)),
    package_data={'src': ['VERSION']},
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)