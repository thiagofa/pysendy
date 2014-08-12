#!/usr/bin/env python
from setuptools import setup, find_packages

version = '0.0.5'

setup(
    name='pysendy',
    version=version,
    description='Sendy API v1.1.7 for Python.',
    long_description=open('README.md').read(),
    author='Thiago Faria de Andrade',
    author_email='thiagofa@gmail.com',
    url='https://github.com/thiagofa/pysendy',
    packages=find_packages(),
    download_url='http://pypi.python.org/pypi/pysendy/',
    keywords='pysendy sendy sendy.co wrapper api',
    zip_safe=True,
    install_requires=['requests'],
    py_modules=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)