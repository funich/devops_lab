#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='snapshot',
    packages=find_packages(),
    version='1.0',
    author='Siarhei_Kuzmich',
    author_email='Siarhei_Kuzmich@epam.com',
    description='Monitoring system',
    install_requires=['psutil'],
    include_package_data=True
)