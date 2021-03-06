#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


PROJECT_ROOT = os.path.dirname(__file__)

with open(os.path.join(PROJECT_ROOT, 'README.rst')) as file_:
    long_description = file_.read()

# Get the version
version_regex = r'__version__ = ["\']([^"\']*)["\']'
with open('hyperframe/__init__.py', 'r') as f:
    text = f.read()
    match = re.search(version_regex, text)

    if match:
        version = match.group(1)
    else:
        raise RuntimeError("No version number found!")

# Stealing this from Kenneth Reitz
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


packages = ['hyperframe']

setup(
    name='hyperframe',
    version=version,
    description='HTTP/2 framing layer for Python',
    long_description=long_description,
    author='Cory Benfield',
    author_email='cory@lukasa.co.uk',
    url='https://python-hyper.org/hyperframe/en/latest/',
    packages=packages,
    package_data={'': ['LICENSE', 'README.rst', 'CONTRIBUTORS.rst', 'HISTORY.rst']},
    package_dir={'hyperframe': 'hyperframe'},
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
