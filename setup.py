# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='bst',
    version='0.0.1',
    description='Example Binary Search Tree',
    long_description=readme,
    author='Stu Jones',
    author_email='stujo',
    url='https://github.com/stujo/python-binary-search-tree',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

